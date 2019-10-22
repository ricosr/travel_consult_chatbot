# -*- coding:utf-8 -*-

# intent: plan ticket

from NLU.plan import ticket_nlu
from NLU.common import give_up_nlu

from NLG.plan import ticket_nlg
from NLG.common import confirm_nlg
from NLG.common import give_up_nlg

from slots.plan_slot import plan_ticket_slot


def plan_ticket_handle(customer_utterance, state_tracker_obj, entities, lac, intent_model, senta_gru, confirm_interpreter, db_obj, collection_name):

    def common_ticket_flow(customer_utterance, state_tracker_obj, entities, lac, db_obj, collection_name):
        give_up_state = give_up_nlu.whether_give_up(customer_utterance, senta_gru, confirm_interpreter)
        if give_up_state:
            state_tracker_obj.update_last_slot_state("stop")
            return give_up_nlg.response_give_up(), "stop"
        else:
            if state_tracker_obj.get_last_slot_state() != "change":
                if state_tracker_obj.get_last_slot_state() == "ask_dept":
                    ie_slot_result = ticket_nlu.ie_all_plan_ticket(customer_utterance, lac, entities, "ask_dept")
                elif state_tracker_obj.get_last_slot_state() == "ask_dest":
                    ie_slot_result = ticket_nlu.ie_all_plan_ticket(customer_utterance, lac, entities, "ask_dest")
                else:
                    ie_slot_result = ticket_nlu.ie_all_plan_ticket(customer_utterance, lac, entities)
            else:
                ie_slot_result = entities
            print("update all", ie_slot_result)
            state_tracker_obj.update_all_state(ie_slot_result)
            slot_state_dict = state_tracker_obj.judge_each_slot_state(plan_ticket_slot.keys())
            # if True not in slot_state_dict.values():
            if slot_state_dict["departure"] is False and slot_state_dict["destination"] is False and slot_state_dict["vehicle"] is False and slot_state_dict["departure_date"] is False:
                state_tracker_obj.update_last_slot_state("ask")
                return ticket_nlg.ask_depart_dest_vehicle_date(), "ask"
            elif slot_state_dict["departure"] is False:
                state_tracker_obj.update_last_slot_state("ask_dept")
                return ticket_nlg.ask_depart(), "ask_dept"
            elif slot_state_dict["destination"] is False:
                state_tracker_obj.update_last_slot_state("ask_dest")
                return ticket_nlg.ask_dest(), "ask_dest"
            elif slot_state_dict["vehicle"] is False:
                state_tracker_obj.update_last_slot_state("ask")
                return ticket_nlg.ask_vehicle(), "ask"
            else:
                # search_ticket_dict_results = db_obj.search_db(collection_name, state_tracker_obj.get_all_confident_slot_values())  # TODO: database
                search_ticket_dict_results = {}    # TODO
                state_tracker_obj.add_one_state("solutions", search_ticket_dict_results, 1)
            state_tracker_obj.update_last_slot_state("confirm_select")
            return ticket_nlg.response_traffic_list(search_ticket_dict_results), "confirm"

    def common_personal_info():   # TODO
        pass

    last_slot_state = state_tracker_obj.get_last_slot_state()
    if last_slot_state == "select_done":
        return common_personal_info()  # TODO: slot 5 and 6
    elif last_slot_state == "confirm_select":
        confirm_state, temp_entities = ticket_nlu.select_plan_ticket(customer_utterance, lac, intent_model, senta_gru, confirm_interpreter, state_tracker_obj.get_confident_slot_value("solutions"))
        print(5, confirm_state, temp_entities)
        if confirm_state == "select_done":
            state_tracker_obj.update_last_slot_state("select_done")
            state_tracker_obj.add_one_state("solution_no", temp_entities, 1)
            return common_personal_info()  # TODO
        if confirm_state == "no":
            state_tracker_obj.update_last_slot_state("ask")
            return confirm_nlg.response_no("plan_ticket", state_tracker_obj.get_all_confident_slot_values()), "ask"
        if confirm_state == "stop":
            state_tracker_obj.update_last_slot_state("stop")
            return confirm_nlg.response_give_up(), "stop"
        if confirm_state == "change":
            state_tracker_obj.update_last_slot_state("change")
            return common_ticket_flow(customer_utterance, state_tracker_obj, temp_entities, lac, db_obj, collection_name)
        if confirm_state == "nothing" or confirm_state == "yes":
            state_tracker_obj.update_last_slot_state("confirm")
            return confirm_nlg.response_nothing(), "confirm"
    elif last_slot_state == "confirm_ticket":
        pass
    else:
         return common_ticket_flow(customer_utterance, state_tracker_obj, entities, lac, db_obj, collection_name)
