# -*- coding: utf-8 -*-

from NLU.consult.dinning_nlu import dinning_nlu_rule
from NLG.consult.dinning_nlg import nlg_confirm_conditions, nlg_recommend_restaurant, nlg_confirm_each_slot, reply_dict


# def dialogue_state(current_slot):
#     values_ls = list(current_slot.values())
#     if None in values_ls or 0 in values_ls:
#         return False
#     else:
#         return True    # all slots are OK


def dinning_flow(current_slot):
    # if yes_no == "negative":
    #     if last_slot_state == 0 and not current_slot["restaurant"]:
    #         current_slot["restaurant"] = yes_no
    #     if last_slot_state == 1 and current_slot["food"] == 0:
    #         current_slot["food"] = yes_no
    #     if last_slot_state == 2 and current_slot["area"] == 0:
    #         current_slot["area"] = yes_no
    #     if last_slot_state == 3 and current_slot["price"] == 0:
    #         current_slot["price"] = yes_no
    #         return None, 3

    for key, value in current_slot.items():
        if not value or value == 0:
            return reply_dict[key][0], key
    # if not current_slot["restaurant"]:
    #     return reply_dict["restaurant"][0], last_slot_state   # TODO: add random
    # if current_slot["food"] == 0:
    #     last_slot_state = 1
    #     return reply_dict[last_slot_state][0], last_slot_state
    # if current_slot["area"] == 0:
    #     last_slot_state = 2
    #     return reply_dict[last_slot_state][0], last_slot_state
    # if current_slot["price"] == 0:
    #     last_slot_state = 3
    #     return reply_dict[last_slot_state][0], last_slot_state
    return None, -1


def dinning_handle(current_slot, customer_utterance, state_tracker_obj, db_obj, collection_name):
    last_slot_state = state_tracker_obj.get_last_slot_state()
    ie_values_dict, yes_no = dinning_nlu_rule(customer_utterance)

    # #############################tackle answer yes or no and for each slot confirm S##############################
    if last_slot_state in current_slot and yes_no:
        if yes_no == "positive":
            if last_slot_state in state_tracker_obj.get_state():
                state_tracker_obj.update_confidence(last_slot_state, 1)
                state_tracker_obj.get_current_slot(current_slot)
                response_utterance, last_slot_state = dinning_flow(current_slot)
                if last_slot_state != -1:
                    state_tracker_obj.update_last_slot_state(last_slot_state)
                    return response_utterance
        if yes_no == "negative":
            if last_slot_state in state_tracker_obj.get_state():
                state_tracker_obj.update_confidence(last_slot_state, 0)
                state_tracker_obj.get_current_slot(current_slot)
            else:
                print("nonoononononon")
                state_tracker_obj.add_one_state(last_slot_state, "no", 1)
                state_tracker_obj.get_current_slot(current_slot)
            response_utterance, last_slot_state = dinning_flow(current_slot)
            if last_slot_state != -1:
                state_tracker_obj.update_last_slot_state(last_slot_state)
                return response_utterance
    # #############################tackle answer yes or no and for each slot confirm E##############################

    # #############################tackle final confirm S##############################
    if yes_no == "positive" and last_slot_state == "done":
        result_ls = db_obj.read_db(collection_name, current_slot)
        state_tracker_obj.update_last_slot_state("done")
        return nlg_recommend_restaurant(result_ls, last_slot_state)
    if yes_no == "negative" and last_slot_state == "done":
        if not ie_values_dict:
            response_utterance, last_slot_state = dinning_flow(current_slot)
            state_tracker_obj.update_last_slot_state(last_slot_state)
            return response_utterance
        else:
            state_tracker_obj.update_last_slot_state("change")
            return "Do you have any other requirements?"
    # #############################tackle final confirm E##############################

    # #############################tackle change slot S##############################
    if yes_no == "positive" and last_slot_state == "change":
        if not ie_values_dict:
            response_utterance, last_slot_state = dinning_flow(current_slot)
            if last_slot_state != -1:
                state_tracker_obj.update_last_slot_state(last_slot_state)
                return response_utterance
    if yes_no == "negative" and last_slot_state == "change":
        result_ls = db_obj.read_db(collection_name, current_slot)
        return nlg_recommend_restaurant(result_ls, last_slot_state)
    # #############################tackle change slot E##############################

    state_tracker_obj.update_all_state(ie_values_dict)    # update dialogue state for all slots
    state_tracker_obj.get_current_slot(current_slot)      # fill and get current slots

    # #############################confirm for each slot S##############################
    need_confirm_slot_ls = state_tracker_obj.get_need_to_confirm()
    if need_confirm_slot_ls:   # need to confirm for each slot
        if last_slot_state not in need_confirm_slot_ls:    # start
            state_tracker_obj.update_last_slot_state(need_confirm_slot_ls[0])
            return nlg_confirm_each_slot(need_confirm_slot_ls[0], current_slot[need_confirm_slot_ls[0]])
        else:
            return nlg_confirm_each_slot(last_slot_state, state_tracker_obj.get_slot_value(last_slot_state))
    # #############################confirm for each slot E##############################

    state = state_tracker_obj.judge_dialogue_state()    # judge whether the filling slots process is done

    if state is True:   # all slots are done
        condition_confirm_utterance = nlg_confirm_conditions(current_slot)
        state_tracker_obj.update_last_slot_state("done")
        return condition_confirm_utterance
    else:   # not done
        response_utterance, last_slot_state = dinning_flow(current_slot)
        state_tracker_obj.update_last_slot_state(last_slot_state)
        # if last_slot_state == "done":
        #     result_ls = db_obj.read_db(collection_name, current_slot)
        #     return nlg_recommend_restaurant(result_ls, last_slot_state)
        # state = state_tracker_obj.judge_dialogue_state()
        # if state is True:
        #     condition_confirm_utterance = nlg_confirm_conditions(current_slot)
        #     return condition_confirm_utterance
    return response_utterance
