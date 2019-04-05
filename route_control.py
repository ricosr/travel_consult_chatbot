# -*- coding: utf-8 -*-

import copy

from intent import judge_intent
from state_tracker import *
from config.config import intent_config, slot_config, database_address, database_name
from oprate_database import Database


def get_input():    # TODO
    pass


def response():    # TODO
    pass


def distribute_task():    # TODO
    pass


def control():
    db_obj = Database(database_address, database_name)
    print("<<<Can I help you?")
    current_intent = ''
    just_sentence = False
    current_intent_slot_dict = {}
    intent_state_tracker_dict = {}
    if_case_no = None
    while True:
        customer_utterance = input(">>>")    # TODO: temp
        intent = judge_intent.judge_intent(customer_utterance)
        # if intent and intent not in current_intent_slot_dict:
        #     current_intent_slot_dict[intent] = ''

        if intent:
            current_intent = intent
        else:
            just_sentence = True

        if intent in current_intent_slot_dict:
            current_slot = current_intent_slot_dict[intent]
        else:
            current_intent_slot_dict[current_intent] = copy.deepcopy(slot_config[current_intent])
            current_slot = current_intent_slot_dict[current_intent]

        handle_function = intent_config[current_intent]

        if intent in intent_state_tracker_dict:
            if_case_no = intent_state_tracker_dict[intent]

        out_content, current_slot, if_case_no = handle_function(current_slot, customer_utterance, intent_state_tracker_dict, just_sentence, if_case_no, db_obj)
        intent_state_tracker_dict[intent] = if_case_no
        current_intent_slot_dict[current_intent] = current_slot
        print(out_content)    # TODO: temp


control()
