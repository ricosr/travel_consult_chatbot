# -*- coding:utf-8 -*-

# intent: consult_weather

from NLU.consult import weather_nlu
from NLU.common import give_up_nlu

from NLG.consult import weather_nlg
from NLG.common import confirm_nlg
from NLG.common import give_up_nlg

from slots.consult_slot import consult_weather_slot
from request_api.consult_weather import request_weather_interface


def consult_weather_handle(customer_utterance, state_tracker_obj, entities, lac, intent_model, senta_gru, confirm_interpreter, db_obj, city_ls):

    def ie_weather_state_flow(customer_utterance, state_tracker_obj, entities, city_ls):
        give_up_state = give_up_nlu.whether_give_up(customer_utterance, senta_gru, confirm_interpreter)
        if give_up_state:
            state_tracker_obj.update_last_slot_state("stop")
            return give_up_nlg.response_give_up(), "stop"
        else:
            if state_tracker_obj.get_last_slot_state() is not "change":
                ie_slot_result = weather_nlu.ie_city_date(customer_utterance, city_ls)
            else:
                ie_slot_result = entities
            state_tracker_obj.update_all_state(ie_slot_result)

            slot_state_dict = state_tracker_obj.judge_each_slot_state(consult_weather_slot.keys())
            if slot_state_dict["city"] is False and slot_state_dict["date"] is False:
                state_tracker_obj.update_last_slot_state("ask")
                return weather_nlg.ask_city_date(), "ask"
            elif slot_state_dict["city"] is False:
                state_tracker_obj.update_last_slot_state("ask")
                return weather_nlg.ask_city(), "ask"
            elif slot_state_dict["date"] is False:
                state_tracker_obj.update_last_slot_state("ask")
                return weather_nlg.ask_date(), "ask"
            else:
                print(state_tracker_obj.get_all_confident_slot_values())
                state_tracker_obj.update_last_slot_state("confirm")
                weather_result = request_weather_interface(state_tracker_obj.get_confident_slot_value("city"), state_tracker_obj.get_confident_slot_value("date"))
                return weather_nlg.response_weather_result(weather_result, state_tracker_obj.get_all_confident_slot_values()), "confirm"

    last_slot_state = state_tracker_obj.get_last_slot_state()
    print(last_slot_state)
    if last_slot_state != "confirm":
        return ie_weather_state_flow(customer_utterance, state_tracker_obj, entities, city_ls)
    else:
        confirm_state, temp_entities = weather_nlu.confirm_consult_weather(customer_utterance, confirm_interpreter, senta_gru, city_ls)
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
            return ie_weather_state_flow(customer_utterance, state_tracker_obj, temp_entities, city_ls)
        if confirm_state == "nothing":
            state_tracker_obj.update_last_slot_state("confirm")
            return confirm_nlg.response_nothing("consult_weather"), "confirm"
