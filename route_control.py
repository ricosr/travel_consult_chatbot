# -*- coding: utf-8 -*-

import paddlehub as hub
from rasa.nlu.model import Interpreter

from intent import judge_intent
from state_tracker import State
from config.config import handle_config, slot_config, database_address, database_name, db_collection_config, intent_model_name, confirm_model_name
from oprate_database import Database


def get_input():    # TODO
    pass


def response():    # TODO
    pass


def distribute_task():    # TODO
    pass


def control():
    lac = hub.Module(name="lac")
    # db_obj = Database(database_address, database_name)    # TODO: database
    db_obj = ''
    intent_model = judge_intent.Intent(intent_model_name)
    confirm_interpreter = Interpreter.load("intent/{}/nlu".format(confirm_model_name))
    senta_gru = hub.Module(name="senta_gru")
    print("<<<您想咨询什么？吃饭还是出行？")
    current_intent = ''
    # just_sentence = False
    # current_intent_slot_dict = {}
    intent_state_tracker_dict = {}
    state_no = None
    while True:
        entities = None
        customer_utterance = input(">>>")    # TODO: temp
        if not current_intent:
            intent, entities = intent_model.get_intent(customer_utterance)
            print(entities)
            current_intent = intent
        else:
            intent, entities = intent_model.get_intent(customer_utterance)
            print(2, entities)
        # if intent and intent not in current_intent_slot_dict:
        #     current_intent_slot_dict[intent] = ''

        # if intent:
        #     current_intent = intent
        # else:
        #     just_sentence = True

        # if intent in current_intent_slot_dict:
        #     current_slot = current_intent_slot_dict[intent]
        # else:
        #     current_intent_slot_dict[current_intent] = copy.deepcopy(slot_config[current_intent])
        #     current_slot = current_intent_slot_dict[current_intent]

        handle_function = handle_config[current_intent]

        # if intent in intent_state_tracker_dict:
        #     state_no = intent_state_tracker_dict[intent]
        if current_intent not in intent_state_tracker_dict:
            intent_state_tracker_dict[current_intent] = State(None)

        collection_name = db_collection_config[current_intent]

        out_content, state = handle_function(customer_utterance, intent_state_tracker_dict[current_intent], entities, lac, intent_model, senta_gru, confirm_interpreter, db_obj, collection_name)
        # intent_state_tracker_dict[intent] = state_no
        # current_intent_slot_dict[current_intent] = current_slot
        # current_intent = intent
        print(out_content)    # TODO: temp
        if state == "stop" or state == "yes":
            intent_state_tracker_dict.pop(current_intent)
            current_intent = ''
            collection_name = ''





control()
