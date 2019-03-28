# -*- coding: utf-8 -*-

from NLU.consult.dinning_nlu import dinning_nlu_rule


def dinning_flow(current_slot, customer_utterance, just_sentence, if_case_no):
    ie_values_dict, yes_no = dinning_nlu_rule(customer_utterance)
    if just_sentence:
        if if_case_no == 0:
            if just_sentence == 'no':
                current_slot["restaurant"] = 'no'
        if if_case_no == 1:
            current_slot["food_drink"] = 'no'
        if if_case_no == 2:
            current_slot["area"] = 'no'
        if if_case_no == 3:
            current_slot["price"] = 'no'
    else:
        for k,v in ie_values_dict.items():
            if v:
                current_slot[k] = v

    if not current_slot["restaurant"]:
        if_case_no = 0
        return "Do you prefer some specific food?"
    if current_slot["food_drink"] == 0:
        if_case_no = 1
        return "Do you prefer some specific food?"
    if current_slot["area"] == 0:
        if_case_no = 2
        return "Do you have demand about the distance from the restaurant?"
    if current_slot["price"] == 0:
        if_case_no = 3
        return "Do you have requirement about the average price?", if_case_no


def dinning_handle(current_slot, customer_utterance, just_sentence):
    if just_sentence:
        pass
    else:
        pass
