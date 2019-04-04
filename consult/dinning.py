# -*- coding: utf-8 -*-

from NLU.consult.dinning_nlu import dinning_nlu_rule
from NLG.consult.dinning_nlg import nlg_confirm_conditions, nlg_chose_restaurant, reply_dict


def dialogue_state(current_slot):    # TODO: temp, dialogue state
    values_ls = list(current_slot.values())
    if None in values_ls or 0 in values_ls:
        return False
    else:
        return True    # all slots are OK


def dinning_flow(current_slot, customer_utterance, just_sentence, if_case_no, yes_no):
    if yes_no == "no":
        if if_case_no == 0 and not current_slot["restaurant"]:
            current_slot["restaurant"] = yes_no
        if if_case_no == 1 and current_slot["food"] == 0:
            current_slot["food"] = yes_no
        if if_case_no == 2 and current_slot["area"] == 0:
            current_slot["area"] = yes_no
        if if_case_no == 3 and current_slot["price"] == 0:
            current_slot["price"] = yes_no
            return None, 3

    if not current_slot["restaurant"]:
        if_case_no = 0
        return reply_dict[if_case_no], if_case_no
    if current_slot["food"] == 0:
        if_case_no = 1
        return reply_dict[if_case_no], if_case_no
    if current_slot["area"] == 0:
        if_case_no = 2
        return reply_dict[if_case_no], if_case_no
    if current_slot["price"] == 0:
        if_case_no = 3
        return reply_dict[if_case_no], if_case_no
    return None, -1

# def confirm_conditions(current_slot):


def dinning_handle(current_slot, customer_utterance, just_sentence, if_case_no, db_obj):
    ie_values_dict, yes_no = dinning_nlu_rule(customer_utterance)
    if yes_no == "yes" and if_case_no == 4:
        # 1.search database 2.nlg
        restaurant_ls = db_obj.read_db("restaurant", current_slot)

        # restaurant_ls = ["abcd", "efg", "hig", "klm"]   # TODO: temp
        return nlg_chose_restaurant(restaurant_ls, if_case_no), current_slot, if_case_no
    if yes_no == 'no' and if_case_no == 4:
        if not ie_values_dict:
            response_utterance, if_case_no = dinning_flow(current_slot, customer_utterance, just_sentence, if_case_no, yes_no)
            return response_utterance, current_slot, if_case_no
        else:
            return "Do you have any other requirements?", current_slot, if_case_no

    for k, v in ie_values_dict.items():
        if v and v != 0:    # TODO: state tracker
            current_slot[k] = v
    state = dialogue_state(current_slot)
    if state is True:
        condition_confirm_utterance = nlg_confirm_conditions(current_slot)
        return condition_confirm_utterance, current_slot, 4
    else:
        response_utterance, if_case_no = dinning_flow(current_slot, customer_utterance, just_sentence, if_case_no, yes_no)
        if if_case_no == -1:
            restaurant_ls = db_obj.read_db("restaurant", current_slot)
            # restaurant_ls = ["abcd", "efg", "hig", "klm"]  # TODO: temp search database
            return nlg_chose_restaurant(restaurant_ls, if_case_no), current_slot, if_case_no
        state = dialogue_state(current_slot)
        if state is True:
            condition_confirm_utterance = nlg_confirm_conditions(current_slot)
            return condition_confirm_utterance, current_slot, 4
    return response_utterance, current_slot, if_case_no
