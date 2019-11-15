# -*- coding: utf-8 -*-

import time

from slots.consult_slot import consult_traffic_slot
from NLU.common import confirm_nlu
from NLU.consult.consult_nlu_key_terms import consult_traffic_key_terms


departure_destination_term_tag = ["LOC", "ORG", "PER", "ns", "nr", "nz", "f", "s", "nt", "nw"]  # n
vehicle_term_tag = ["n", "nz", "v"]
departure_time_term_tag = ["TIME", "t"]


def judge_all_entities(ie_values_dict):
    if not ie_values_dict:
        return False
    ie_keys = ie_values_dict.keys()
    for slot_key in consult_traffic_slot.keys():
        if slot_key not in ie_keys:
            return False
    return True


def paddle_lac(text, lac):
    lac_inputs = {"text": [text]}
    lac_result_dict = lac.lexical_analysis(data=lac_inputs)[0]
    return lac_result_dict


def convert_zh_to_num(time_text):
    if "现" in time_text:
        return time.strftime("%H-%M", time.localtime(time.time()))
    num_dict = {"一": "1", "二": "2", "两": "2", "三": "3", "四": "4", "五": "5", "六": "6", "七": "7", "八": "8", "九": "9", "零": "0", "十":''}
    for time_mark in consult_traffic_key_terms["time_mark"]:
        time_text = time_text.replace(time_mark, '-').strip('-')
    tmp_num_ls = time_text.split('-')
    num_judge = True
    for each_num in tmp_num_ls:
        for key in num_dict:
            if key in each_num:
                num_judge = False
                break
    if num_judge is True:
        return '-'.join(tmp_num_ls)

    for index in range(len(tmp_num_ls)):
        try:
            int(tmp_num_ls[index])
        except Exception as e:
            tmp_num = ''
            if '十' in tmp_num_ls[index]:
                if tmp_num_ls[index][0] == '十':
                    tmp_num = tmp_num_ls[index].replace('十', '1')
                    if len(tmp_num_ls[index]) == 1:
                        tmp_num += '0'
                elif len(tmp_num_ls[index]) > 1:
                    if tmp_num_ls[index][1] == '十':
                        tmp_num = tmp_num_ls[index].replace('十', '0')
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
    print('-'.join(tmp_num_ls))
    return '-'.join(tmp_num_ls)


def ie_all_consult_traffic(customer_utterance, lac, entities, ask_type=None):
    customer_tmp_utterance = customer_utterance.replace('：', ':').replace('-', ':').replace('.', ':')
    ie_values_dict = {}
    lac_result_dict = paddle_lac(customer_tmp_utterance, lac)
    print("traffic nlu lac", lac_result_dict)
    departure_time = ''
    for tag_index in range(len(lac_result_dict["tag"])):
        if lac_result_dict["tag"][tag_index] in departure_time_term_tag:
            print("time1", lac_result_dict["word"][tag_index])
            departure_time = lac_result_dict["word"][tag_index]
            try:
                if lac_result_dict["tag"][tag_index+1] == 'm':
                    departure_time += lac_result_dict["word"][tag_index+1]
            except Exception as e:
                pass
            ie_values_dict["departure_time"] = convert_zh_to_num(departure_time)
            break

    if entities:
        for entity in entities:
            if entity["entity"] == "departure" and entity["value"].replace('：', ':').replace('-', ':').replace('.', ':') not in departure_time:
                # if entity["value"] in lac_result_dict["word"]:
                #     if lac_result_dict["tag"][lac_result_dict["word"].index(entity["value"])] in departure_destination_term_tag:
                #         ie_values_dict["departure"] = entity["value"]
                # else:
                if ask_type == "ask_dest":
                    ie_values_dict["destination"] = entity["value"]
                else:
                    ie_values_dict["departure"] = entity["value"]
            if entity["entity"] == "destination" and entity["value"].replace('：', ':').replace('-', ':').replace('.', ':') not in departure_time:
                # if entity["value"] in lac_result_dict["word"]:
                #     if lac_result_dict["tag"][lac_result_dict["word"].index(entity["value"])] in departure_destination_term_tag:
                #         ie_values_dict["destination"] = entity["value"]
                # else:
                if ask_type == "ask_dept":
                    ie_values_dict["departure"] = entity["value"]
                else:
                    ie_values_dict["destination"] = entity["value"]
            if entity["entity"] == "hotel" and entity["value"].replace('：', ':').replace('-', ':').replace('.', ':') not in departure_time:
                if entity["value"] in lac_result_dict["word"]:
                    if lac_result_dict["tag"](lac_result_dict["word"].index(entity["value"])) in departure_destination_term_tag:
                        if ask_type == "ask_dept":
                            ie_values_dict["departure"] = entity["value"]
                        else:
                            ie_values_dict["destination"] = entity["value"]
            if entity["entity"] == "vehicle" and entity["value"].replace('：', ':').replace('-', ':').replace('.', ':') not in departure_time:
                print(entity["entity"])
                for vehicle, terms_ls in consult_traffic_key_terms["vehicle_terms"].items():
                    for term in terms_ls:
                        if (entity["value"] in term or term in entity["value"]) and len(customer_utterance) > 1:
                            ie_values_dict["vehicle"] = vehicle
                            break
                    if "vehicle" in ie_values_dict:
                        break
    # if not judge_all_entities(ie_values_dict):
    if True:    # TODO: exchange rule and rasa
        if len(lac_result_dict["tag"]) == 1 and lac_result_dict["tag"][0] in departure_destination_term_tag:
            if ask_type == "ask_dept":
                ie_values_dict["departure"] = customer_tmp_utterance
            else:
                ie_values_dict["destination"] = customer_tmp_utterance
            return ie_values_dict
        temp_tag_point = 0
        for tag_index in range(len(lac_result_dict["tag"])):
            continue_key = False
            if lac_result_dict["tag"][tag_index] in departure_destination_term_tag:
                print(lac_result_dict["tag"][tag_index])
                if 'p' in lac_result_dict["tag"][temp_tag_point: tag_index] or tag_index == 0:
                    ie_values_dict["departure"] = lac_result_dict["word"][tag_index]
                    continue_key = True
                    temp_tag_point = tag_index + 1
                    tmp_tag_ls = lac_result_dict["tag"][tag_index+1:]
                    tmp_word_ls = lac_result_dict["word"][tag_index+1:]
                    for tag_i in range(len(tmp_tag_ls)):
                        if tmp_tag_ls[tag_i] in departure_destination_term_tag or tmp_tag_ls[tag_i] == 'n':    # and "departure" not in ie_values_dict:  # TODO: rule is good? or rasa?
                            ie_values_dict["departure"] += tmp_word_ls[tag_i]
                            temp_tag_point += 1
                        else:
                            break
                else:
                    print(lac_result_dict["tag"][temp_tag_point: tag_index])
                    if 'v' in lac_result_dict["tag"][temp_tag_point: tag_index]:
                        v_index = lac_result_dict["tag"][temp_tag_point:tag_index].index('v')
                    elif "vd" in lac_result_dict["tag"][temp_tag_point: tag_index]:
                        v_index = lac_result_dict["tag"][temp_tag_point: tag_index].index("vd")
                    elif "vn" in lac_result_dict["tag"][temp_tag_point: tag_index]:
                        v_index = lac_result_dict["tag"][temp_tag_point: tag_index].index("vn")
                    else:
                        v_index = False
                    if v_index is not False:
                        print("des lac:", lac_result_dict["tag"][temp_tag_point: tag_index+1][v_index:])
                        ie_values_dict["destination"] = lac_result_dict["word"][tag_index]
                        continue_key = True
                        temp_tag_point = tag_index + 1
                        tmp_tag_ls = lac_result_dict["tag"][tag_index + 1:]
                        tmp_word_ls = lac_result_dict["word"][tag_index + 1:]
                        for tag_i in range(len(tmp_tag_ls)):
                            if tmp_tag_ls[tag_i] in departure_destination_term_tag or tmp_tag_ls[tag_i] == 'n':  # and "departure" not in ie_values_dict:  # TODO: rule is good? or rasa?
                                ie_values_dict["destination"] += tmp_word_ls[tag_i]
                                temp_tag_point += 1
                            else:
                                break
                if ask_type == "ask_dept":
                    ie_values_dict["departure"] = lac_result_dict["word"][tag_index]
                    tmp_tag_ls = lac_result_dict["tag"][tag_index + 1:]
                    tmp_word_ls = lac_result_dict["word"][tag_index + 1:]
                    for tag_i in range(len(tmp_tag_ls)):
                        if tmp_tag_ls[tag_i] in departure_destination_term_tag or tmp_tag_ls[tag_i] == 'n':  # and "departure" not in ie_values_dict:  # TODO: rule is good? or rasa?
                            ie_values_dict["departure"] += tmp_word_ls[tag_i]
                            temp_tag_point += 1
                        else:
                            break
                    break
                if ask_type == "ask_dest":
                    ie_values_dict["destination"] = lac_result_dict["word"][tag_index]
                    tmp_tag_ls = lac_result_dict["tag"][tag_index + 1:]
                    tmp_word_ls = lac_result_dict["word"][tag_index + 1:]
                    for tag_i in range(len(tmp_tag_ls)):
                        if tmp_tag_ls[tag_i] in departure_destination_term_tag or tmp_tag_ls[tag_i] == 'n':  # and "departure" not in ie_values_dict:  # TODO: rule is good? or rasa?
                            ie_values_dict["destination"] += tmp_word_ls[tag_i]
                            temp_tag_point += 1
                        else:
                            break
                    break
                if continue_key is True:
                    continue
            if lac_result_dict["tag"][tag_index] in vehicle_term_tag:
                for vehicle, terms_ls in consult_traffic_key_terms["vehicle_terms"].items():
                    for term in terms_ls:
                        if lac_result_dict["word"][tag_index] in term or term in lac_result_dict["word"][tag_index] and "vehicle" not in ie_values_dict:
                            ie_values_dict["vehicle"] = vehicle
                            continue_key = True
                            break
                    if "vehicle" in ie_values_dict:
                        break
                if continue_key is True:
                    continue
            if lac_result_dict["tag"][tag_index] in departure_time_term_tag:
                print("time2", lac_result_dict["word"][tag_index])
                departure_time = lac_result_dict["word"][tag_index]
                try:
                    if lac_result_dict["tag"][tag_index + 1] == 'm':
                        departure_time += lac_result_dict["word"][tag_index + 1]
                except Exception as e:
                    pass
                ie_values_dict["departure_time"] = convert_zh_to_num(departure_time)
                continue_key = True
                if continue_key is True:
                    continue

    return ie_values_dict


# def ie_departure_time(customer_utterance, lac):
#     customer_tmp_utterance = customer_utterance.replace('：', ':')
#     lac_result_dict = paddle_lac(customer_tmp_utterance, lac)
#     for tag_index in range(len(lac_result_dict["tag"])):
#         if lac_result_dict["tag"][tag_index] in departure_time_term_tag:
#             return convert_zh_to_num(lac_result_dict["word"][tag_index])
#     return False


def confirm_consult_traffic(customer_utterance, lac, intent_model, senta_gru, confirm_interpreter):
    intent, entities = intent_model.get_intent(customer_utterance)
    ie_slot_result = ie_all_consult_traffic(customer_utterance, lac, entities)
    if ie_slot_result:
        return "change", ie_slot_result
    confirm_state = confirm_nlu.judge_confirm_classification(customer_utterance, senta_gru, confirm_interpreter)
    print(confirm_state)
    return confirm_state, None


# convert_zh_to_num("十一点50")

