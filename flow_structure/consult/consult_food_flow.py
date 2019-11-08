# -*- coding:utf-8 -*-

# intent: consult_food

from NLU.consult import food_nlu
from NLU.common import give_up_nlu

from NLG.consult import food_nlg
from NLG.common import confirm_nlg
from NLG.common import give_up_nlg

from slots.consult_slot import consult_food_slot
from db_operation.food_db import search_consult_food


def consult_food_handle(customer_utterance, state_tracker_obj, entities, lac, intent_model, senta_gru, confirm_interpreter, db_obj, collection_name):

    def ie_food_state_flow(customer_utterance, state_tracker_obj, entities, lac, db_obj, collection_name):
        give_up_state = give_up_nlu.whether_give_up(customer_utterance, senta_gru, confirm_interpreter)
        if give_up_state:
            state_tracker_obj.update_last_slot_state("stop")
            return give_up_nlg.response_give_up(), "stop"
        else:
            if state_tracker_obj.get_last_slot_state() is not"change":
                ie_slot_result = food_nlu.ie_all_consult_food(customer_utterance, lac, entities)
            else:
                ie_slot_result = entities
            state_tracker_obj.update_all_state(ie_slot_result)

            slot_state_dict = state_tracker_obj.judge_each_slot_state(consult_food_slot.keys())
            if slot_state_dict["food"] is False and slot_state_dict["restaurant"] is False:
                state_tracker_obj.update_last_slot_state("ask")
                return food_nlg.ask_food_restaurant(), "ask"
            else:
                search_restaurants_results = search_consult_food(state_tracker_obj.get_all_confident_slot_values(), db_obj.get_db_conn()[collection_name])
                # print(state_tracker_obj.get_all_confident_slot_values())
                # search_restaurants_results = ''
                print(search_restaurants_results)
                state_tracker_obj.update_last_slot_state("confirm")
                return food_nlg.response_restaurant_list(search_restaurants_results, state_tracker_obj.get_all_confident_slot_values()), "confirm"

    last_slot_state = state_tracker_obj.get_last_slot_state()
    print(last_slot_state)
    if last_slot_state != "confirm":
        return ie_food_state_flow(customer_utterance, state_tracker_obj, entities, lac, db_obj, collection_name)
    else:
        confirm_state, temp_entities = food_nlu.confirm_consult_food(customer_utterance, lac, intent_model, senta_gru, confirm_interpreter)
        print(5, confirm_state, temp_entities)
        if confirm_state == "yes":
            state_tracker_obj.update_last_slot_state("stop")
            return confirm_nlg.response_yes(), "stop"
        if confirm_state == "no":
            state_tracker_obj.update_last_slot_state("ask")
            return confirm_nlg.response_no("consult_food", state_tracker_obj.get_all_confident_slot_values()), "ask"
        if confirm_state == "stop":
            state_tracker_obj.update_last_slot_state("stop")
            return confirm_nlg.response_give_up(), "stop"
        if confirm_state == "change":
            state_tracker_obj.update_last_slot_state("change")
            return ie_food_state_flow(customer_utterance, state_tracker_obj, temp_entities, lac, db_obj, collection_name)
        if confirm_state == "nothing":
            state_tracker_obj.update_last_slot_state("confirm")
            return confirm_nlg.response_nothing("consult_food"), "confirm"










