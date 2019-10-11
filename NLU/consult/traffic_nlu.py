# -*- coding: utf-8 -*-

from slots.consult_slot import consult_traffic_slot
from NLU.common import confirm_nlu

departure_term_tag = []
destination_term_tag = []
vehicle_term_tag = []
departure_time_term_tag = []


def judge_all_entities(ie_values_dict):
    if not ie_values_dict:
        return False
    slot_keys = consult_traffic_slot.keys()
    for ie_key, v in ie_values_dict.items():
        if ie_key not in slot_keys:
            return False
    return True


def paddle_lac(text, lac):
    lac_inputs = {"text": [text]}
    lac_result_dict = lac.lexical_analysis(data=lac_inputs)[0]
    return lac_result_dict


def ie_all_search_food(customer_utterance, lac, entities):
    pass


def ie_departure_time(customer_utterance, lac, entities):
    pass
