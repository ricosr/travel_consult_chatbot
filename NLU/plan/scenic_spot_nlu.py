# -*- coding: utf-8 -*-


from slots.plan_slot import plan_scenic_spot_slot
from NLU.common import confirm_nlu
# from plan_nlu_key_terms import plan_ticket_key_terms


departure_destination_term_tag = ["LOC", "ORG", "PER", "ns", "nr", "nz", "f", "s", "nt", "nw"]  # n


def judge_all_entities(ie_values_dict):
    if not ie_values_dict:
        return False
    ie_keys = ie_values_dict.keys()
    for slot_key in plan_scenic_spot_slot.keys():
        if slot_key not in ie_keys:
            return False
    return True


def paddle_lac(text, lac):
    lac_inputs = {"text": [text]}
    lac_result_dict = lac.lexical_analysis(data=lac_inputs)[0]
    return lac_result_dict


def convert_to_num(utterance):
    num_dict = {"一": "1", "二": "2", "两": "2", "三": "3", "四": "4", "五": "5", "六": "6", "七": "7", "八": "8", "九": "9"}
    for key, value in num_dict.items():
        if key in utterance:
            utterance = utterance.replace(key, value)
    return utterance

