# -*- coding:utf-8 -*-

# intent: plan scenic spot

from NLU.plan import scenic_spot_nlu
from NLU.common import give_up_nlu

from NLG.plan import scenic_spot_nlg
from NLG.common import confirm_nlg
from NLG.common import give_up_nlg

from slots.plan_slot import plan_scenic_spot_slot


def plan_scenic_spot_handle(customer_utterance, state_tracker_obj, entities, lac, intent_model, senta_gru, confirm_interpreter, db_obj, collection_name):

    def common_scenic_spot_flow(customer_utterance, state_tracker_obj, entities, lac, db_obj, collection_name):
        give_up_state = give_up_nlu.whether_give_up(customer_utterance, senta_gru, confirm_interpreter)
        if give_up_state:
            state_tracker_obj.update_last_slot_state("stop")
            return give_up_nlg.response_give_up(), "stop"
        else:
            if state_tracker_obj.get_last_slot_state() != "change":
                ie_slot_result = scenic_spot_nlu.ie_all_plan_scenic_spot(customer_utterance, lac, entities)
            else:
                ie_slot_result = entities
            state_tracker_obj.update_all_state(ie_slot_result)

            slot_state_dict = state_tracker_obj.judge_each_slot_state(plan_scenic_spot_slot.keys())
            if slot_state_dict["city"] is False and slot_state_dict["days"] is False:
                state_tracker_obj.update_last_slot_state("ask")
                return scenic_spot_nlg.ask_city_days(), "ask"
            elif slot_state_dict["city"] is False:
                state_tracker_obj.update_last_slot_state("ask")
                return scenic_spot_nlg.ask_city(), "ask"
            elif slot_state_dict["days"] is False:
                state_tracker_obj.update_last_slot_state("ask")
                return scenic_spot_nlg.ask_days(), "ask"
            else:
                # search_scheme_dict_results = db_obj.search_db(collection_name, state_tracker_obj.get_all_confident_slot_values())  # TODO: database
                search_scheme_dict_results = {
                    1: "旅游方案1",
                    2: "旅游方案2",
                    3: "旅游方案3",
                    4: "旅游方案4"
                }  # TODO
                state_tracker_obj.add_one_state("schemes", search_scheme_dict_results, 1)
                print("start to select schemes")
                state_tracker_obj.update_last_slot_state("confirm_select")
                print("common last state", state_tracker_obj.get_last_slot_state())
                return scenic_spot_nlg.response_scheme_list(search_scheme_dict_results), "confirm_select"

    def common_personal_info_flow(customer_utterance, state_tracker_obj, lac):
        give_up_state = give_up_nlu.whether_give_up(customer_utterance, senta_gru, confirm_interpreter)
        if give_up_state:
            state_tracker_obj.update_last_slot_state("stop")
            return give_up_nlg.response_give_up(), "stop"
        pass

    last_slot_state = state_tracker_obj.get_last_slot_state()
    print("last_slot_state:", last_slot_state)
    if last_slot_state != "confirm_select":
        return common_scenic_spot_flow(customer_utterance, state_tracker_obj, entities, lac, db_obj, collection_name)
    else:
        confirm_state, temp_entities = scenic_spot_nlu.confirm_plan_scenic_spot(customer_utterance, lac, intent_model, senta_gru, confirm_interpreter, state_tracker_obj.get_confident_slot_value("schemes"))
        print(5, confirm_state, temp_entities)
        if confirm_state == "yes":
            state_tracker_obj.update_last_slot_state("stop")
            return confirm_nlg.response_yes(), "yes"
        if confirm_state == "no":
            state_tracker_obj.update_last_slot_state("ask")
            return confirm_nlg.response_no("plan_scenic_spot", state_tracker_obj.get_all_confident_slot_values()), "ask"
        if confirm_state == "stop":
            state_tracker_obj.update_last_slot_state("stop")
            return confirm_nlg.response_give_up(), "stop"
        if confirm_state == "change":
            state_tracker_obj.update_last_slot_state("change")
            return common_scenic_spot_flow(customer_utterance, state_tracker_obj, temp_entities, lac, db_obj, collection_name)
        if confirm_state == "nothing":
            state_tracker_obj.update_last_slot_state("confirm_select")
            return confirm_nlg.response_nothing(), "confirm_select"
