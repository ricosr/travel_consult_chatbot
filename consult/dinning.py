# -*- coding: utf-8 -*-

from NLU.consult.dinning_nlu import dinning_nlu_rule


def slot_state(current_slot):
    if len(current_slot) > current_slot.values():
        return False


def dinning_flow(current_slot, customer_utterance, just_sentence, if_case_no):
    ie_values_dict, yes_no = dinning_nlu_rule(customer_utterance)
    if yes_no:
        if if_case_no == 0:
            current_slot["restaurant"] = yes_no
        if if_case_no == 1:
            current_slot["food_drink"] = yes_no
        if if_case_no == 2:
            current_slot["area"] = yes_no
        if if_case_no == 3:
            current_slot["price"] = yes_no
    else:
        for k, v in ie_values_dict.items():
            if v:    # TODO: state tracker
                current_slot[k] = v

    if not current_slot["restaurant"]:
        if_case_no = 0
        return "Do you prefer some specific food?", if_case_no
    if current_slot["food_drink"] == 0:
        if_case_no = 1
        return "Do you prefer some specific food?", if_case_no
    if current_slot["area"] == 0:
        if_case_no = 2
        return "Do you have demand about the distance from the restaurant?", if_case_no
    if current_slot["price"] == 0:
        if_case_no = 3
        return "Do you have requirement about the average price?", if_case_no



def dinning_handle(current_slot, customer_utterance, just_sentence):

