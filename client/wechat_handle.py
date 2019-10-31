# -*- coding:utf-8 -*-

import logging
import traceback
from random import choice

from gevent.pywsgi import WSGIServer
from gevent import monkey
monkey.patch_all()
import falcon
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException
from wechatpy import parse_message
from wechatpy.replies import TextReply


from rule_based_common_nlg import rule_response
from request_client import load_clients, select_consult_client, select_plan_client
from util.translate_l import translate
from util.language import punctuation_ls


logging.basicConfig(filename='logger.log', level=logging.INFO)
logging.debug('debug message')


class Connect:
    def __init__(self, consult_ip, plan_ip, wechat_token):
        load_clients(consult_ip, plan_ip)
        self.wechat_token = wechat_token
        self.user_state = {}

    def judge_language(self, message):
        for each_char in message:
            if each_char in punctuation_ls or each_char == ' ' or each_char == '\t' or each_char == '\n':
                continue
            else:
                if not 'A' < each_char < 'z':
                    return 'zh'
        return 'en'

    def on_get(self, req, resp):
        # print("get_req:{}".format(req))
        query_string = req.query_string
        query_list = query_string.split('&')
        b = {}
        for i in query_list:
            b[i.split('=')[0]] = i.split('=')[1]

        try:
            check_signature(token=self.wechat_token, signature=b['signature'], timestamp=b['timestamp'], nonce=b['nonce'])
            resp.body = (b['echostr'])
        except InvalidSignatureException:
            pass
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        xml = req.stream.read()
        msg = parse_message(xml)
        from_user_name = self.extract_from_username(msg)
        input_language_zh = True
        if len(self.cache_dict) > 200:
            self.cache_dict = {}
        if msg.type == 'text':
            inputTxt = msg.content
            language = self.judge_language(inputTxt)
            if language == 'en':
                input_language_zh = False
                inputTxt = translate(inputTxt, 'en')
            replyTxt, reply_type = self.getReply(inputTxt, msg.id, input_language_zh, from_user_name)
            reply = TextReply(content=replyTxt, message=msg)
            xml = reply.render()
            resp.body = (xml)
            resp.status = falcon.HTTP_200

    def extract_from_username(self, msg):
        msg_para_ls = str(msg).split("), (")
        from_user_name_index = 1
        for index in range(len(msg_para_ls)):
            if "FromUserName" in msg_para_ls[index]:
                from_user_name_index = index
                break
        from_user_name = msg_para_ls[from_user_name_index].split(',')[1].strip('\'')
        return from_user_name

    def getReply(self, utterance, msg_id, input_language_zh, from_user_name):
        default_reply = ["什么什么什么？没听懂", "我没理解你的意思，可以具体一点吗？", "主人，你在讲啥子嘛？", "我太笨，你能换个说法吗？"]
        try:
            response_msg = rule_response(utterance)
            if not response_msg:
                if utterance == "咨询":   # TODO
                    # recoder user consult state
                    return "请提问..."
                if utterance == "规划":
                    # recoder user plan state
                    return "请选择1,2,3.。。"
                if utterance == "订票":
                    pass
                if utterance == "攻略":
                    pass
                client_obj, client_no = select_consult_client()    # TODO: how to select for different tasks
                response_msg = client_obj.get_response(utterance, client_no, msg_id, from_user_name)
            logging.info(response_msg + "none")
            if input_language_zh is False and self.judge_language(response_msg) == "zh":
                response_msg = translate(response_msg, 'zh')
            if response_msg:
                return response_msg, "norm"
            else:
                logging.info(response_msg + "none")
                return choice(default_reply), "none"
        except Exception as e:
            logging.error(traceback.format_exc())
            return choice(default_reply), "err"


if __name__ == '__main__':
    consult_ip = "tcp://127.0.0.1:10086"
    plan_ip = "tcp://127.0.0.1:10010"
    wechat_token = "1234567"
    app = falcon.API()
    app.add_route('/', Connect(consult_ip, plan_ip, wechat_token))
    server = WSGIServer(('0.0.0.0', 80), app)
    server.serve_forever()