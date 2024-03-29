# -*- coding: utf-8 -*-

import copy
import time

import paddlehub as hub
from rasa.nlu.model import Interpreter
# from rasa_nlu.model import Interpreter

from intent import judge_intent
from state_tracker import State
from config.config import handle_config, plan_intent_ls, database_address, database_name, db_collection_config, intent_model_name, confirm_model_name, time_out, db_record_collection_config
from db_operation.oprate_database import Database
from NLG.plan.plan_start_nlg import ask_start_plan
from NLU.consult.weather_nlu import load_city


class Consult:
    def __init__(self):
        self.lac = hub.Module(name="lac")
        self.confirm_interpreter = Interpreter.load("intent/{}/nlu".format(confirm_model_name))
        self.senta_gru = hub.Module(name="senta_gru")
        self.db_obj = Database(database_address, database_name)
        self.intent_model = judge_intent.Intent(intent_model_name)
        self.city_ls = load_city("static/city.json")
        self.user_dict = {}
        self.user_timeout_recoder = {}

    def start_cmd(self):
        print("<<<您想咨询什么？吃饭？出行？天气？")
        while True:
            utterance = input(">>>")
            if utterance.strip() == "exit1":
                break
            answer = self.get_answer(utterance, "123456")
            print("<<<{}".format(answer))

    def get_answer(self, customer_utterance, user_id):
        if user_id in self.user_dict:
            if int(time.time()) - self.user_timeout_recoder[user_id] > time_out:
                self.user_dict.pop(user_id)
            else:
                self.user_timeout_recoder[user_id] = int(time.time())
        if user_id not in self.user_dict:
            self.user_dict[user_id] = {"current_intent": '', "intent_state_tracker_dict": {}}
            self.user_timeout_recoder[user_id] = int(time.time())

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

        if current_intent == "consult_weather":
            collection_name = self.city_ls
        else:
            collection_name = db_collection_config[current_intent]

        out_content, state = handle_function(customer_utterance, self.user_dict[user_id]["intent_state_tracker_dict"][current_intent], entities, self.lac, self.intent_model, self.senta_gru, self.confirm_interpreter, self.db_obj, collection_name)

        if state == "stop":
            # self.user_dict[user_id]["intent_state_tracker_dict"].pop(current_intent)
            # self.user_dict[user_id]["current_intent"] = ''
            self.user_dict.pop(user_id)

        return out_content + "@---@" + state

# control_obj = Consult()
# control_obj.start_cmd()


class Plan:
    def __init__(self):
        self.lac = hub.Module(name="lac")
        self.confirm_interpreter = Interpreter.load("intent/{}/nlu".format(confirm_model_name))
        self.senta_gru = hub.Module(name="senta_gru")
        self.db_obj = Database(database_address, database_name)
        self.intent_model = judge_intent.Intent(intent_model_name)
        self.user_dict = {}
        self.user_timeout_recoder = {}

    def start_cmd(self):
        print("<<<请您回答我的问题，以便给你做出规划，谢谢！")
        while True:
            utterance = input(">>>")
            if utterance.strip() == "exit1":
                break
            answer = self.get_answer(utterance, "", "123456")
            print("<<<{}".format(answer))

    def get_answer(self, customer_utterance, plan_intent, user_id):
        current_intent = ''
        if user_id in self.user_dict:
            if int(time.time()) - self.user_timeout_recoder[user_id] > time_out:
                self.user_dict.pop(user_id)
            else:
                self.user_timeout_recoder[user_id] = int(time.time())
        if user_id not in self.user_dict:
            if plan_intent:
                self.user_dict[user_id] = {"current_intent": plan_intent, "intent_state_tracker_dict": {}, "plan_intent": ''}
                current_intent = self.user_dict[user_id]["current_intent"]
                self.user_timeout_recoder[user_id] = int(time.time())
            else:  # for start_cmd
                self.user_dict[user_id] = {"current_intent": '', "intent_state_tracker_dict": {}, "plan_intent": copy.copy(plan_intent_ls)}
                self.user_timeout_recoder[user_id] = int(time.time())
        else:
            current_intent = self.user_dict[user_id]["current_intent"]
            self.user_timeout_recoder[user_id] = int(time.time())

        if not current_intent:
            self.user_dict[user_id]["current_intent"] = self.user_dict[user_id]["plan_intent"][0]
            current_intent = self.user_dict[user_id]["current_intent"]
            return ask_start_plan(current_intent)

        intent, entities = self.intent_model.get_intent(customer_utterance)
        handle_function = handle_config[current_intent]

        if plan_intent:
            if plan_intent not in self.user_dict[user_id]["intent_state_tracker_dict"]:
                self.user_dict[user_id]["intent_state_tracker_dict"][current_intent] = State(None)
        else:
            if current_intent not in self.user_dict[user_id]["intent_state_tracker_dict"]:
                self.user_dict[user_id]["intent_state_tracker_dict"][current_intent] = State(None)

        collection_name = db_collection_config[current_intent]

        out_content, state = handle_function(customer_utterance,
                                             self.user_dict[user_id]["intent_state_tracker_dict"][current_intent],
                                             entities, self.lac, self.intent_model, self.senta_gru,
                                             self.confirm_interpreter, self.db_obj, collection_name)
        if state == "yes":
            user_collection_name = db_record_collection_config[current_intent]
            if user_collection_name:
                print({user_id: self.user_dict[user_id]["intent_state_tracker_dict"][current_intent].get_all_confident_slot_values()})
                self.db_obj.write_db({user_id: self.user_dict[user_id]["intent_state_tracker_dict"][current_intent].get_all_confident_slot_values()}, user_collection_name)
                self.user_dict.pop(user_id)
            else:
                self.user_dict.pop(user_id)
        if state == "stop":
            print("ffffffffffffffffff", state)
            self.user_dict.pop(user_id)
            # self.user_dict[user_id]["intent_state_tracker_dict"].pop(current_intent)
            # self.user_dict[user_id]["current_intent"] = ''
            # if not plan_intent:
            #     self.user_dict[user_id]["plan_intent"].remove(current_intent)
            # TODO: self.db_conn.write_records

        # if not plan_intent:
        #     if not self.user_dict[user_id]["plan_intent"]:
        #         self.user_dict.pop(user_id)

        return out_content + "@---@" + state

# plan_obj = Plan()
# plan_obj.start_cmd()
