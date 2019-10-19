# -*- coding: utf-8 -*-

import paddlehub as hub
from rasa.nlu.model import Interpreter
import gevent
import zmq.green as zmq

from intent import judge_intent
from state_tracker import State
from config.config import handle_config, slot_config, database_address, database_name, db_collection_config, intent_model_name, confirm_model_name
from oprate_database import Database


class Consult:
    def __init__(self):
        self.lac = hub.Module(name="lac")
        self.confirm_interpreter = Interpreter.load("intent/{}/nlu".format(confirm_model_name))
        self.senta_gru = hub.Module(name="senta_gru")
        # self.db_obj = Database(database_address, database_name)    # TODO: database
        self.db_obj = ''
        self.intent_model = judge_intent.Intent(intent_model_name)
        self.user_dict = {}

    def start_cmd(self):
        print("<<<您想咨询什么？吃饭还是出行？")
        while True:
            utterance = input(">>>")
            if utterance.strip() == "exit1":
                break
            answer = self.get_answer(utterance, "123456")
            print(answer)

    def get_answer(self, customer_utterance, user_id):
        if user_id not in self.user_dict:
            self.user_dict[user_id] = {"current_intent": '', "intent_state_tracker_dict": {}}

        current_intent = self.user_dict[user_id]["current_intent"]
        if not current_intent:
            intent, entities = self.intent_model.get_intent(customer_utterance)
            print(intent, entities)
            current_intent = intent
            self.user_dict[user_id]["current_intent"] = current_intent
        else:
            intent, entities = self.intent_model.get_intent(customer_utterance)
            print(2, entities)
        handle_function = handle_config[current_intent]

        if current_intent not in self.user_dict[user_id]["intent_state_tracker_dict"]:
            self.user_dict[user_id]["intent_state_tracker_dict"][current_intent] = State(None)

        collection_name = db_collection_config[current_intent]

        out_content, state = handle_function(customer_utterance, self.user_dict[user_id]["intent_state_tracker_dict"][current_intent], entities, self.lac, self.intent_model, self.senta_gru, self.confirm_interpreter, self.db_obj, collection_name)

        if state == "stop" or state == "yes":
            self.user_dict[user_id]["intent_state_tracker_dict"].pop(current_intent)
            self.user_dict[user_id]["current_intent"] = ''

        return out_content

control_obj = Consult()
control_obj.start_cmd()


# def control():
#     lac = hub.Module(name="lac")
#     # db_obj = Database(database_address, database_name)    # TODO: database
#     db_obj = ''
#     intent_model = judge_intent.Intent(intent_model_name)
#     confirm_interpreter = Interpreter.load("intent/{}/nlu".format(confirm_model_name))
#     senta_gru = hub.Module(name="senta_gru")
#     print("<<<您想咨询什么？吃饭还是出行？")
#     current_intent = ''
#     intent_state_tracker_dict = {}
#     state_no = None
#     while True:
#         entities = None
#         customer_utterance = input(">>>")
#         if not current_intent:
#             intent, entities = intent_model.get_intent(customer_utterance)
#             print(intent, entities)
#             current_intent = intent
#         else:
#             intent, entities = intent_model.get_intent(customer_utterance)
#             print(2, entities)
#         handle_function = handle_config[current_intent]
#
#         if current_intent not in intent_state_tracker_dict:
#             intent_state_tracker_dict[current_intent] = State(None)
#
#         collection_name = db_collection_config[current_intent]
#
#         out_content, state = handle_function(customer_utterance, intent_state_tracker_dict[current_intent], entities, lac, intent_model, senta_gru, confirm_interpreter, db_obj, collection_name)
#
#         print(out_content)
#         if state == "stop" or state == "yes":
#             intent_state_tracker_dict.pop(current_intent)
#             current_intent = ''
#             collection_name = ''
#
# control()
