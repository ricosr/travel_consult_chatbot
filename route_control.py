# -*- coding: utf-8 -*-

from intent import judge_intent
from config.config import intent_config, slot_config


def get_input():    # TODO
    pass


def response():    # TODO
    pass


def distribute_task():    # TODO
    pass


def control():
    print("<<<Can I help you?")
    current_intent = ''
    just_sentence = False
    current_intent_slot_dict = {}
    while True:
        customer_utterance = input(">>>")    # TODO: temp
        intent = judge_intent.judge_intent(customer_utterance)
        if intent and intent not in current_intent_slot_dict:
            current_intent_slot_dict[intent] = ''

        if intent:
            current_intent = intent
        else:
            just_sentence = True

        if intent in current_intent_slot_dict:
            current_slot = current_intent_slot_dict[intent]
        else:
            current_intent_slot_dict[current_intent] = slot_config[current_intent]
            current_slot = current_intent_slot_dict[current_intent]

        handle_function = intent_config[current_intent]
        out_content, current_slot = handle_function(current_slot, customer_utterance, just_sentence)
        current_intent_slot_dict[current_intent] = current_slot
        print(out_content)    # TODO: temp


control()
