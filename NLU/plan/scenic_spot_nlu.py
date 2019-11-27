# -*- coding: utf-8 -*-

import re

from slots.plan_slot import plan_scenic_spot_slot
from NLU.common import confirm_nlu
from NLU.plan.plan_nlu_key_terms import plan_scenic_spot_key_terms


city_term_tag = ["LOC", "ORG", "ns", "nr", "nz", "f", "s", "nt", "nw"]  # n
time_term_tag = ["m", "q", "TIME", "t"]
absolute_time_term_tag = ["TIME", "t"]


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


def ie_days(utterance):
    utterance = utterance.replace("个礼拜", "周").replace("礼拜", "周")
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
    if re_result:
        tmp_num = re_result.group(0)
        print("tmp num:", tmp_num)
        if int(tmp_num) > 7:
            return False
        if len(utterance) > utterance.index(re_result.group(0))+len(tmp_num):
            if utterance[utterance.index(re_result.group(0))+len(tmp_num)] == "周":
                if int(tmp_num) > 1:
                    return False
                if int(tmp_num) == 1:
                    return 7
        return int(tmp_num)
    else:
        return False


def ie_all_plan_scenic_spot(customer_utterance, lac, entities):
    lac_result_dict = paddle_lac(customer_utterance, lac)
    print("lac_result_dict:", lac_result_dict)
    ie_values_dict = {}
    for tag_index in range(len(lac_result_dict["tag"])):
        if lac_result_dict["tag"][tag_index] in city_term_tag:
            ie_values_dict["city"] = lac_result_dict["word"][tag_index]
            continue
        if lac_result_dict["tag"][tag_index] in time_term_tag:
            nor_num = ie_days(lac_result_dict["word"][tag_index])
            # if nor_num:
            ie_values_dict["days"] = nor_num
            print("ie_values_dict days", ie_values_dict)
    print("ie_values_dict1:", ie_values_dict)
    if not judge_all_entities(ie_values_dict):
        if entities:
            print("entities:", entities)
            if "city" not in ie_values_dict:
                for entity_index in range(len(entities)):
                    if entities[entity_index]["entity"] == "destination":
                        tmp_ie_city = paddle_lac(entities[entity_index]["value"], lac)
                        for tag_index in range(len(tmp_ie_city["tag"])):
                            if tmp_ie_city["tag"][tag_index] in city_term_tag:
                                ie_values_dict["city"] = tmp_ie_city["word"][tag_index]
            if "city" not in ie_values_dict:
                for entity_index in range(len(entities)):
                    if entities[entity_index]["entity"] == "departure":
                        tmp_ie_city = paddle_lac(entities[entity_index]["value"], lac)
                        for tag_index in range(len(tmp_ie_city["tag"])):
                            if tmp_ie_city["tag"][tag_index] in city_term_tag:
                                ie_values_dict["city"] = tmp_ie_city["word"][tag_index]
    if "city" in ie_values_dict:
        for admin_unit1 in plan_scenic_spot_key_terms["admin_unit1"]:
            if admin_unit1 == ie_values_dict["city"][-1]:
                ie_values_dict["city"] = ie_values_dict["city"][:-1]
                break
        for admin_unit2 in plan_scenic_spot_key_terms["admin_unit2"]:
            if admin_unit2 in ie_values_dict["city"]:
                ie_values_dict["city"] = ie_values_dict["city"].replace(admin_unit2, '')
                break
        for admin_unit3 in plan_scenic_spot_key_terms["admin_unit3"]:
            if admin_unit3 == ie_values_dict["city"][-1] and len(ie_values_dict["city"][:-1]) > 1:
                ie_values_dict["city"] = ie_values_dict["city"][:-1]
                break
    print("ie_values_dict2:", ie_values_dict)
    return ie_values_dict


def ie_scheme_no(customer_utterance, scheme_no_list, lac):
    exist_num = False
    lac_result_dict = paddle_lac(customer_utterance, lac)
    for tag_index in range(len(lac_result_dict["tag"])):
        if lac_result_dict["tag"][tag_index] in absolute_time_term_tag:
            return False
        if lac_result_dict["tag"][tag_index] in time_term_tag:
            try:
                if 0 <= int(lac_result_dict["word"][tag_index]) < 100:
                    exist_num = True
                if int(lac_result_dict["word"][tag_index])-1 in scheme_no_list:
                    return int(lac_result_dict["word"][tag_index])
            except Exception as e:
                continue
    if exist_num is True:
        return "overflow"
    for scheme_no in scheme_no_list:
        if str(scheme_no) in customer_utterance:
            return scheme_no
    return False


def confirm_plan_scenic_spot(customer_utterance, lac, intent_model, senta_gru, confirm_interpreter, schemes):
    if schemes:
        scheme_no = ie_scheme_no(customer_utterance, [i for i in range(len(schemes))], lac)
        if scheme_no:
            if scheme_no == "overflow":
                return "nothing", None
            return "yes", scheme_no
    intent, entities = intent_model.get_intent(customer_utterance)
    ie_slot_result = ie_all_plan_scenic_spot(customer_utterance, lac, entities)
    if ie_slot_result:
        return "change", ie_slot_result
    confirm_state = confirm_nlu.judge_confirm_classification(customer_utterance, senta_gru, confirm_interpreter)
    print(confirm_state)
    return confirm_state, None
