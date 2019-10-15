# -*- coding: utf-8 -*-

import time

from slots.consult_slot import consult_traffic_slot
from NLU.common import confirm_nlu
from nlu_key_terms import search_traffic_key_terms


departure_destination_term_tag = ["LOC", "ORG", "PER", "ns", "nr", "nz", "f", "s", "nt", "nw"]
vehicle_term_tag = ["n", "nz", "v"]
departure_time_term_tag = ["TIME", "m", "q", "t"]


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


def convert_to_num(time_text):
    if "现" in time_text:
        return time.strftime("%H:%M", time.localtime(time.time()))
    num_dict = {"一": "1", "二": "2", "两": "2", "三": "3", "四": "4", "五": "5", "六": "6", "七": "7", "八": "8", "九": "9", "零": "0"}
    for time_mark in search_traffic_key_terms["time_mark"]:
        time_text = time_text.replace(time_mark, '-').strip('-')
    tmp_num_ls = time_text.split('-')
    num_judge = True
    for each_num in tmp_num_ls:
        if each_num in num_dict:
            num_judge = False
            break
    if num_judge is True:
        return '-'.join(tmp_num_ls)

    for index in range(len(tmp_num_ls)):
        try:
            int(tmp_num_ls[index])
        except Exception as e:
            if '十' in tmp_num_ls[index]:
                if tmp_num_ls[index][0] == '十':
                    tmp_num = tmp_num_ls[index].replace('十', '1')
                    if len(tmp_num_ls[index]) == 1:
                        tmp_num += '0'
                else:
                    tmp_num = tmp_num_ls[index].replace('十', '')
            else:
                tmp_num = tmp_num_ls[index]
            new_num = ''
            for each_num in tmp_num:
                if each_num in num_dict:
                    new_num += num_dict[each_num]
                else:
                    new_num += each_num
            tmp_num_ls[index] = new_num
    return '-'.join(tmp_num_ls)


def ie_all_search_traffic(customer_utterance, lac, entities):
    customer_tmp_utterance = customer_utterance.replace('：', ':')
    ie_values_dict = {}
    lac_result_dict = paddle_lac(customer_tmp_utterance, lac)
    if entities:
        for entity in entities:
            if entity["entity"] == "departure":
                ie_values_dict["departure"] = entity["value"]
            if entity["entity"] == "destination":
                ie_values_dict["destination"] = entity["value"]
            if entity["entity"] == "hotel":
                ie_values_dict["destination"] = entity["value"]
            if entity["entity"] == "vehicle":
                for vehicle, terms_ls in search_traffic_key_terms["vehicle_terms"].items():
                    for term in terms_ls:
                        if entity["value"] in term or term in entity["value"]:
                            ie_values_dict["vehicle"] = vehicle
                            break
                    if "vehicle" in ie_values_dict:
                        break
    if not judge_all_entities(ie_values_dict):
        if len(lac_result_dict["tag"]) == 1 and lac_result_dict["tag"][0] in departure_destination_term_tag:   # TODO: need to improve
            ie_values_dict["destination"] = customer_tmp_utterance
        for tag_index in range(len(lac_result_dict["tag"])):
            if lac_result_dict["tag"][tag_index] in departure_destination_term_tag:
                departure_judge = True
                if 'p' in lac_result_dict["tag"][: tag_index]:
                    p_index = lac_result_dict["tag"][: tag_index].index('p')
                    for tag in lac_result_dict["tag"][: tag_index][p_index:]:
                        if tag in departure_destination_term_tag:
                            departure_judge = False
                            break
                    if departure_judge is True:
                        ie_values_dict["departure"] = lac_result_dict["word"][tag_index]
                else:
                    destination_judge = True
                    if 'v' in lac_result_dict["tag"][: tag_index]:
                        v_index = lac_result_dict["tag"][: tag_index].index('v')
                    elif "vd" in lac_result_dict["tag"][: tag_index]:
                        v_index = lac_result_dict["tag"][: tag_index].index("vd")
                    elif "vn" in lac_result_dict["tag"][: tag_index]:
                        v_index = lac_result_dict["tag"][: tag_index].index("vn")
                    else:
                        continue
                    for tag in lac_result_dict["tag"][: tag_index][v_index:]:
                        if tag in departure_destination_term_tag:
                            destination_judge = False
                            break
                    if destination_judge is True:
                        ie_values_dict["destination"] = lac_result_dict["word"][tag_index]
                continue
            if lac_result_dict["tag"][tag_index] in vehicle_term_tag:
                for vehicle, terms_ls in search_traffic_key_terms["vehicle_terms"].items():
                    for term in terms_ls:
                        if entity["value"] in term or term in entity["value"]:
                            ie_values_dict["vehicle"] = vehicle
                            break
                    if "vehicle" in ie_values_dict:
                        break
                continue
            if lac_result_dict["tag"][tag_index] in departure_time_term_tag:
                ie_values_dict["departure_time"] = convert_to_num(lac_result_dict["word"][tag_index])

    return ie_values_dict


def ie_departure_time(customer_utterance, lac):
    customer_tmp_utterance = customer_utterance.replace('：', ':')
    lac_result_dict = paddle_lac(customer_tmp_utterance, lac)
    for tag_index in range(len(lac_result_dict["tag"])):
        if lac_result_dict["tag"][tag_index] in departure_time_term_tag:
            return convert_to_num(lac_result_dict["word"][tag_index])
    return False


def confirm_search_traffic(customer_utterance, lac, intent_model, senta_gru, confirm_interpreter):
    intent, entities = intent_model.get_intent(customer_utterance)
    ie_slot_result = ie_all_search_traffic(customer_utterance, lac, entities)
    if ie_slot_result:
        return "change", ie_slot_result
    confirm_state = confirm_nlu.judge_confirm_classification(customer_utterance, senta_gru, confirm_interpreter)
    print(confirm_state)
    return confirm_state, None
