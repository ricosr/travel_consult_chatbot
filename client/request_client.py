# -*- coding: utf-8 -*-

import time
import random

import gevent
import zmq.green as zmq


TIME_OUT = 5000
WAITE_TIME = 10

CONSULT_CLIENT_NUM = 20
CONSULT_CLIENT_BUSY = []
CONSULT_CLIENT_DICT = {}

PLAN_CLIENT_NUM = 20
PLAN_CLIENT_BUSY = []
PLAN_CLIENT_DICT = {}


class Client:
    msg_id = -1

    def __init__(self, server_ip):
        self.context = zmq.Context()
        # self.utterance = None
        self.start_client()
        self.connect_ip = server_ip     #"tcp://127.0.0.1:10086"

    def client(self):
        self.socket = self.context.socket(zmq.REQ)
        self.socket.setsockopt(zmq.LINGER, TIME_OUT)
        self.socket.connect(self.connect_ip)

    def start_client(self):
        client = gevent.spawn(self.client)
        gevent.joinall([client])

    def get_response(self, utterance, client_no, msgid, from_user_name):
        self.socket.send_string(utterance + "@---@" + from_user_name)
        reply = self.socket.recv()

        if reply:
            response = str(reply, encoding="utf-8")
        if Client.msg_id != msgid:    # for timeout
            Client.msg_id = msgid
            while True:
                if response:
                    CONSULT_CLIENT_BUSY.remove(int(client_no))
                    return response
        time.sleep(WAITE_TIME)


def load_clients(consult_ip, plan_ip):
    for i in range(CONSULT_CLIENT_NUM):
        CONSULT_CLIENT_DICT[i] = Client(consult_ip)
    for i in range(PLAN_CLIENT_NUM):
        PLAN_CLIENT_DICT[i] = Client(plan_ip)


def select_consult_client():
    i = random.randint(0, CONSULT_CLIENT_NUM-1)
    while True:
        if i == CONSULT_CLIENT_NUM:
            i = 0
        if i in CONSULT_CLIENT_BUSY:
            i += 1
            continue
        else:
            CONSULT_CLIENT_BUSY.append(i)
            # print(CONSULT_CLIENT_BUSY)
            return CONSULT_CLIENT_DICT[i], i


def select_plan_client():
    i = random.randint(0, PLAN_CLIENT_NUM-1)
    while True:
        if i == PLAN_CLIENT_NUM:
            i = 0
        if i in PLAN_CLIENT_BUSY:
            i += 1
            continue
        else:
            PLAN_CLIENT_BUSY.append(i)
            # print(CONSULT_CLIENT_BUSY)
            return PLAN_CLIENT_DICT[i], i

#
# if __name__ == '__main__':
#     message = ''
#     load_clients()
#     cli, index = select_client("tcp://127.0.0.1:10086)
#     print(cli.get_response(message, index, random.random()), index)
