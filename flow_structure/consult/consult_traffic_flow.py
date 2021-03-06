# -*- coding:utf-8 -*-

# intent: consult_traffic

from NLU.consult import traffic_nlu
from NLU.common import give_up_nlu

from NLG.consult import traffic_nlg
from NLG.common import confirm_nlg
from NLG.common import give_up_nlg

from slots.consult_slot import consult_traffic_slot
from request_api.consult_traffic import get_traffic_route_interface


def consult_traffic_handle(customer_utterance, state_tracker_obj, entities, lac, intent_model, senta_gru, confirm_interpreter, db_obj, collection_name):

    def ie_traffic_state_flow(customer_utterance, state_tracker_obj, entities, lac, db_obj, collection_name):
        give_up_state = give_up_nlu.whether_give_up(customer_utterance, senta_gru, confirm_interpreter)
        if give_up_state:
            state_tracker_obj.update_last_slot_state("stop")
            return give_up_nlg.response_give_up(), "stop"
        else:
            if state_tracker_obj.get_last_slot_state() != "change":
                if state_tracker_obj.get_last_slot_state() == "ask_dept":
                    ie_slot_result = traffic_nlu.ie_all_consult_traffic(customer_utterance, lac, entities, "ask_dept")
                elif state_tracker_obj.get_last_slot_state() == "ask_dest":
                    ie_slot_result = traffic_nlu.ie_all_consult_traffic(customer_utterance, lac, entities, "ask_dest")
                else:
                    ie_slot_result = traffic_nlu.ie_all_consult_traffic(customer_utterance, lac, entities)
            else:
                ie_slot_result = entities
            print("update all", ie_slot_result)
            state_tracker_obj.update_all_state(ie_slot_result)
            slot_state_dict = state_tracker_obj.judge_each_slot_state(consult_traffic_slot.keys())
            # if True not in slot_state_dict.values():
            if slot_state_dict["departure"] is False and slot_state_dict["destination"] is False and slot_state_dict["vehicle"] is False:
                state_tracker_obj.update_last_slot_state("ask")
                return traffic_nlg.ask_depart_dest_vehicle(), "ask"
            elif slot_state_dict["departure"] is False:
                state_tracker_obj.update_last_slot_state("ask_dept")
                return traffic_nlg.ask_depart(), "ask_dept"
            elif slot_state_dict["destination"] is False:
                state_tracker_obj.update_last_slot_state("ask_dest")
                return traffic_nlg.ask_dest(), "ask_dest"
            elif slot_state_dict["vehicle"] is False:
                state_tracker_obj.update_last_slot_state("ask")
                return traffic_nlg.ask_vehicle(), "ask"
            else:
                pass
                # ie_time_result = traffic_nlu.ie_departure_time(customer_utterance, lac)
                # if ie_time_result:
                #     if state_tracker_obj.get_confident_slot_value("departure_time"):
                #         state_tracker_obj.update_slot_value("departure_time", ie_slot_result)
                #         state_tracker_obj.update_confidence("departure_time", 1)
                #     else:
                #         if state_tracker_obj.get_slot_value("departure_time") == ie_time_result:
                #             state_tracker_obj.update_confidence("departure_time", 1)
                #         else:
                #             state_tracker_obj.add_one_state("departure_time", ie_slot_result, 1)

            # search_traffic_results = db_conn.search_db(collection_name, state_tracker_obj.get_all_confident_slot_values())
            search_traffic_results = get_traffic_route_interface(state_tracker_obj.get_all_confident_slot_values())
            state_tracker_obj.update_last_slot_state("confirm")
            return traffic_nlg.response_traffic_list(search_traffic_results, state_tracker_obj.get_all_confident_slot_values()), "confirm"

    last_slot_state = state_tracker_obj.get_last_slot_state()
    if last_slot_state != "confirm":
        return ie_traffic_state_flow(customer_utterance, state_tracker_obj, entities, lac, db_obj, collection_name)
    else:
        confirm_state, temp_entities = traffic_nlu.confirm_consult_traffic(customer_utterance, lac, intent_model, senta_gru, confirm_interpreter)
        print(5, confirm_state, temp_entities)
        if confirm_state == "yes":
            state_tracker_obj.update_last_slot_state("stop")
            return confirm_nlg.response_yes(), "stop"
        if confirm_state == "no":
            state_tracker_obj.update_last_slot_state("ask")
            return confirm_nlg.response_no("consult_traffic", state_tracker_obj.get_all_confident_slot_values()), "ask"
        if confirm_state == "stop":
            state_tracker_obj.update_last_slot_state("stop")
            return confirm_nlg.response_termination(), "stop"
        if confirm_state == "change":
            state_tracker_obj.update_last_slot_state("change")
            return ie_traffic_state_flow(customer_utterance, state_tracker_obj, temp_entities, lac, db_obj, collection_name)
        if confirm_state == "nothing":
            state_tracker_obj.update_last_slot_state("confirm")
            return confirm_nlg.response_uncertain("consult_traffic"), "confirm"
