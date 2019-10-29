# -*- coding: utf-8 -*-

import re

from slots.plan_slot import plan_scenic_spot_slot
from NLU.common import confirm_nlu
# from plan_nlu_key_terms import plan_ticket_key_terms


city_term_tag = ["LOC", "ORG", "PER", "ns", "nr", "nz", "f", "s", "nt", "nw"]  # n
departure_time_term_tag = ["m", "q", "TIME", "t"]


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


def normalize_num(utterance):
    large_num = ['十', '百', '千', '万']
    for num in large_num:
        if num in utterance:
            return False
    num_dict = {"一": "1", "二": "2", "两": "2", "三": "3", "四": "4", "五": "5", "六": "6", "七": "7", "八": "8", "九": "9", "零": "0"}
    for key, value in num_dict.items():
        if key in utterance:
            utterance = utterance.replace(key, value)
    re_pattern = re.compile("[0-9]+")
    re_result = re_pattern.search(utterance)
    if int(re_result.group(0)) > 7:
        return False
    return utterance


def ie_all_plan_scenic_spot(customer_utterance, lac, entities, ask_type=None):
    lac_result_dict = paddle_lac(customer_utterance, lac)
    ie_values_dict = {}
    for tag_index in range(len(lac_result_dict["tag"])):
        if lac_result_dict["tag"][tag_index] in city_term_tag:
            ie_values_dict["city"] = lac_result_dict["word"][tag_index]
            continue
        if lac_result_dict["tag"][tag_index] in departure_time_term_tag:
            nor_num = normalize_num(lac_result_dict["word"][tag_index])
            if nor_num:
                ie_values_dict["days"] = nor_num
    if not judge_all_entities(ie_values_dict):
        if entities:
            if "city" not in ie_values_dict:
                for entity_index in entities:
                    if entities[entity_index]["entity"] == "destination":
                        ie_values_dict["city"] = entities[entity_index]["value"]
            if "city" not in ie_values_dict:
                for entity_index in entities:
                    if entities[entity_index]["entity"] == "departure":
                        ie_values_dict["city"] = entities[entity_index]["value"]

    return ie_values_dict


def ie_scheme_no(customer_utterance, solution_no_list):   # TODO: temp method
    for solution_no in solution_no_list:
        if str(solution_no) in customer_utterance:
            return solution_no
    return False


def confirm_plan_scenic_spot(customer_utterance, lac, intent_model, senta_gru, confirm_interpreter, solutions):
    solution_no = ie_scheme_no(customer_utterance, solutions.keys())
    if solution_no:
        return "yes", solution_no
    intent, entities = intent_model.get_intent(customer_utterance)
    ie_slot_result = ie_all_plan_scenic_spot(customer_utterance, lac, entities)
    if ie_slot_result:
        return "change", ie_slot_result
    confirm_state = confirm_nlu.judge_confirm_classification(customer_utterance, senta_gru, confirm_interpreter)
    print(confirm_state)
    return confirm_state, None
