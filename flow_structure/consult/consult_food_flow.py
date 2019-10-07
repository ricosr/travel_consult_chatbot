# -*- coding:utf-8 -*-

from NLU.consult import food_nlu
from NLU.common import confirm_nlu
from NLU.common import give_up_nlu

from NLG.consult import food_nlg
from NLG.common import confirm_nlg
from NLG.common import give_up_nlg

from slots.consult_slot import consult_food_slot


def consult_food_handle(current_slot, customer_utterance, state_tracker_obj, entities, lac, intent_model, senta_gru, confirm_interp_model, db_obj, collection_name):

    def common_food_flow(current_slot, customer_utterance, state_tracker_obj, entities, lac, db_obj, collection_name):
        give_up_state = give_up_nlu.whether_give_up(customer_utterance)
        if give_up_state:
            state_tracker_obj.update_last_slot_state("stop")
            return give_up_nlg.response_give_up(), "stop"
        else:
            if state_tracker_obj.get_last_slot_state() is not"change":
                ie_slot_result = food_nlu.ie_all_search_food(customer_utterance, lac, entities)
            else:
                ie_slot_result = entities
            state_tracker_obj.update_all_state(ie_slot_result)

            slot_state_dict = state_tracker_obj.judge_each_slot_state(consult_food_slot.keys())
            if True not in slot_state_dict.values():
                state_tracker_obj.update_last_slot_state("ask")
                return food_nlg.ask_food_restaurant(), "ask"
            else:
                search_restaurants_results = db_obj.search_db(collection_name, state_tracker_obj.get_all_confident_slot_values())  # TODO
                state_tracker_obj.update_last_slot_state("confirm")
                return food_nlg.response_restaurant_list(search_restaurants_results), "confirm"  # TODO

    last_slot_state = state_tracker_obj.get_last_slot_state()
    if last_slot_state is not "confirm":
        return common_food_flow(current_slot, customer_utterance, state_tracker_obj, entities, lac, db_obj, collection_name)
    else:
        confirm_state, temp_entities = food_nlu.confirm_search_food(customer_utterance, lac, intent_model, senta_gru, confirm_interp_model)
        if confirm_state is "yes":
            state_tracker_obj.update_last_slot_state("stop")
            return confirm_nlg.response_yes(), "stop"
        if confirm_state is "no":
            state_tracker_obj.update_last_slot_state("ask")
            return confirm_nlg.response_no(), "ask"
        if confirm_state is "stop":
            state_tracker_obj.update_last_slot_state("stop")
            return confirm_nlg.response_give_up(), "stop"
        if confirm_state is "change":
            state_tracker_obj.update_last_slot_state("change")
            return common_food_flow(current_slot, customer_utterance, state_tracker_obj, temp_entities, lac, db_obj, collection_name)
        if confirm_state is "nothing":
            state_tracker_obj.update_last_slot_state("confirm")
            return confirm_nlg.response_nothing(), "confirm"










