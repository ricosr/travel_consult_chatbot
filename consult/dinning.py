# -*- coding: utf-8 -*-

from NLU.consult.dinning_nlu import dinning_nlu_rule
from NLG.consult.dinning_nlg import nlg_confirm_conditions, nlg_chose_restaurant, nlg_confirm_each_slot, reply_dict


# def dialogue_state(current_slot):
#     values_ls = list(current_slot.values())
#     if None in values_ls or 0 in values_ls:
#         return False
#     else:
#         return True    # all slots are OK


def dinning_flow(current_slot, customer_utterance, just_sentence, if_case_no, yes_no):
    if yes_no == "negative":
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
        return reply_dict[if_case_no][0], if_case_no   # TODO: add random
    if current_slot["food"] == 0:
        if_case_no = 1
        return reply_dict[if_case_no][0], if_case_no
    if current_slot["area"] == 0:
        if_case_no = 2
        return reply_dict[if_case_no][0], if_case_no
    if current_slot["price"] == 0:
        if_case_no = 3
        return reply_dict[if_case_no][0], if_case_no
    return None, -1


def dinning_handle(current_slot, customer_utterance, state_tracker_obj, just_sentence, db_obj, collection_name):
    last_slot_key = state_tracker_obj.get_last_slot_key()
    ie_values_dict, yes_no = dinning_nlu_rule(customer_utterance)

    if yes_no == "positive" and last_slot_key == "done":    # TODO: 0405, the same way to 0,1,2,3
        result_ls = db_obj.read_db(collection_name, current_slot)
        return nlg_chose_restaurant(result_ls, last_slot_key), current_slot, last_slot_key
    if yes_no == 'negative' and last_slot_key == "done":
        if not ie_values_dict:
            response_utterance, last_slot_key = dinning_flow(current_slot, customer_utterance, just_sentence, last_slot_key, yes_no)
            return response_utterance, current_slot, last_slot_key
        else:
            return "Do you have any other requirements?", current_slot, last_slot_key

    state_tracker_obj.update_all_state(ie_values_dict)
    state_tracker_obj.get_current_slot(current_slot)
    need_confirm_slot = state_tracker_obj.get_need_to_confirm()
    if need_confirm_slot:
        return nlg_confirm_each_slot(last_slot_key)    #  last_slot_key???????

    state = state_tracker_obj.judge_dialogue_state()

    if state is True:
        condition_confirm_utterance = nlg_confirm_conditions(current_slot)
        state_tracker_obj.update_last_slot_key("done")
        return condition_confirm_utterance
    else:
        response_utterance, last_slot_key = dinning_flow(current_slot, customer_utterance, just_sentence, last_slot_key, yes_no)
        state_tracker_obj.update_last_slot_key(last_slot_key)
        # if last_slot_key == "done":
        #     result_ls = db_obj.read_db(collection_name, current_slot)
        #     return nlg_chose_restaurant(result_ls, last_slot_key)
        # state = state_tracker_obj.judge_dialogue_state()
        # if state is True:
        #     condition_confirm_utterance = nlg_confirm_conditions(current_slot)
        #     return condition_confirm_utterance
    return response_utterance
