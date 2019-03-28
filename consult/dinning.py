# -*- coding: utf-8 -*-

from NLU.consult.dinning_nlu import dinning_nlu_rule
from NLG.consult.dinning_nlg import nlg_confirm_conditions, nlg_chose_restaurant


def dialogue_state(current_slot):    # TODO: temp, dialogue state
    values_ls = list(current_slot.values())
    if None in values_ls or 0 in values_ls:
        return False
    else:
        return True    # all slots are OK


def dinning_flow(current_slot, customer_utterance, just_sentence, if_case_no, yes_no):
    if yes_no:
        if if_case_no == 0:
            current_slot["restaurant"] = yes_no
        if if_case_no == 1:
            current_slot["food_drink"] = yes_no
        if if_case_no == 2:
            current_slot["area"] = yes_no
        if if_case_no == 3:
            current_slot["price"] = yes_no

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

# def confirm_conditions(current_slot):


def dinning_handle(current_slot, customer_utterance, just_sentence, if_case_no):
    ie_values_dict, yes_no = dinning_nlu_rule(customer_utterance)
    if yes_no == "yes" and if_case_no == 4:
        # 1.search database 2.nlg
        restaurant_ls = []   # TODO: temp
        return nlg_chose_restaurant(restaurant_ls)
    elif yes_no == 'no' and if_case_no == 4:
        if not ie_values_dict:
            pass    # nlg
    else:
        pass

    for k, v in ie_values_dict.items():
        if v:    # TODO: state tracker
            current_slot[k] = v
    state = dialogue_state(current_slot)
    if state is True:
        condition_confirm_utterance = nlg_confirm_conditions(current_slot)
        return condition_confirm_utterance, current_slot, 4
    else:
        response_utterance, if_case_no = dinning_flow(current_slot, customer_utterance, just_sentence, if_case_no, yes_no)
    return response_utterance, if_case_no
