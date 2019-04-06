# -*- coding: utf-8 -*-

from NLU.consult.dinning_nlu import dinning_nlu_rule
from NLG.consult.dinning_nlg import nlg_confirm_conditions, nlg_recommend_restaurant, nlg_confirm_each_slot, dinning_reply


def judge_confirm_each_slot(state_tracker_obj, last_slot_state, current_slot, yes_no):
    if last_slot_state in current_slot and yes_no:
        if yes_no == "positive":
            if last_slot_state in state_tracker_obj.get_state():
                state_tracker_obj.update_confidence(last_slot_state, 1)
                state_tracker_obj.get_current_slot(current_slot)
                response_utterance, last_slot_state = dinning_reply(current_slot)
                if last_slot_state != -1:
                    state_tracker_obj.update_last_slot_state(last_slot_state)
                    return response_utterance
        if yes_no == "negative":
            if last_slot_state in state_tracker_obj.get_state():
                state_tracker_obj.update_slot_value(last_slot_state, "no")
                state_tracker_obj.update_confidence(last_slot_state, 1)
                state_tracker_obj.get_current_slot(current_slot)
            else:
                state_tracker_obj.add_one_state(last_slot_state, "no", 1)
                state_tracker_obj.get_current_slot(current_slot)
            response_utterance, last_slot_state = dinning_reply(current_slot)
            if last_slot_state:
                state_tracker_obj.update_last_slot_state(last_slot_state)
                return response_utterance


def final_confirm(ie_values_dict, current_slot, state_tracker_obj, last_slot_state, yes_no, db_obj, collection_name):
    if yes_no == "positive" and last_slot_state == "done":
        result_ls = db_obj.read_db(collection_name, current_slot)
        state_tracker_obj.update_last_slot_state("done")
        return nlg_recommend_restaurant(result_ls, last_slot_state)
    if yes_no == "negative" and last_slot_state == "done":
        if ie_values_dict:
            response_utterance, last_slot_state = dinning_reply(current_slot)
            state_tracker_obj.update_last_slot_state(last_slot_state)
            state_tracker_obj.update_all_state(ie_values_dict)  # update dialogue state for all slots
            state_tracker_obj.get_current_slot(current_slot)  # fill and get current slots
            return response_utterance
        else:
            state_tracker_obj.update_last_slot_state("change")
            return "Do you have any other requirements?"


def change_slot(state_tracker_obj, current_slot, ie_values_dict, last_slot_state, yes_no, db_obj, collection_name):
    if yes_no == "positive" and last_slot_state == "change":
        if not ie_values_dict:
            state_tracker_obj.update_last_slot_state(None)
            return "your requirements?"
            # response_utterance, last_slot_state = dinning_reply(current_slot)
            # if last_slot_state:
            #     state_tracker_obj.update_last_slot_state(last_slot_state)
            #     return response_utterance
    if yes_no == "negative" and last_slot_state == "change":
        result_ls = db_obj.read_db(collection_name, current_slot)
        return nlg_recommend_restaurant(result_ls, last_slot_state)


def confirm_each_slot(state_tracker_obj, last_slot_state):
    need_confirm_slot_ls = state_tracker_obj.get_need_to_confirm()
    if need_confirm_slot_ls:  # need to confirm for each slot
        if last_slot_state not in need_confirm_slot_ls:  # start
            state_tracker_obj.update_last_slot_state(need_confirm_slot_ls[0])
            return nlg_confirm_each_slot(need_confirm_slot_ls[0],
                                         state_tracker_obj.get_slot_value(need_confirm_slot_ls[0]))
        else:
            return nlg_confirm_each_slot(last_slot_state, state_tracker_obj.get_slot_value(last_slot_state))


def dinning_handle(current_slot, customer_utterance, state_tracker_obj, db_obj, collection_name):
    last_slot_state = state_tracker_obj.get_last_slot_state()
    ie_values_dict, yes_no = dinning_nlu_rule(customer_utterance)
    print(last_slot_state, ie_values_dict, yes_no)

    response_utterance = judge_confirm_each_slot(state_tracker_obj, last_slot_state, current_slot, yes_no)
    if response_utterance:
        return response_utterance

    response_utterance = final_confirm(ie_values_dict, current_slot, state_tracker_obj, last_slot_state, yes_no, db_obj, collection_name)
    if response_utterance:
        return response_utterance

    response_utterance = change_slot(state_tracker_obj, current_slot, ie_values_dict, last_slot_state, yes_no, db_obj, collection_name)
    if response_utterance:
        return response_utterance

    print(state_tracker_obj.get_state())
    state_tracker_obj.update_all_state(ie_values_dict)    # update dialogue state for all slots
    state_tracker_obj.get_current_slot(current_slot)      # fill and get current slots
    print(state_tracker_obj.get_state())
    print(current_slot)

    response_utterance = confirm_each_slot(state_tracker_obj, last_slot_state)
    if response_utterance:
        return response_utterance

    state = state_tracker_obj.judge_dialogue_state()    # judge whether the filling slots process is done

    if state is True:   # all slots are done
        condition_confirm_utterance = nlg_confirm_conditions(current_slot)
        state_tracker_obj.update_last_slot_state("done")
        return condition_confirm_utterance
    else:   # not done
        response_utterance, last_slot_state = dinning_reply(current_slot)
        state_tracker_obj.update_last_slot_state(last_slot_state)
    return response_utterance
