# -*- coding: utf-8 -*-

import json

from NLU.common import confirm_nlu
from NLU.consult.consult_nlu_key_terms import consult_weather_key_terms


def load_city(city_file):
    with open(city_file, "r") as fw:
        data = fw.read()
    city_list = []
    json_data = json.loads(data)
    for each in json_data:
        city_list.append(each["cityZh"])
    return city_list


def ie_city_date(customer_utterance, city_ls):
    ie_values_dict = {}
    for city in city_ls:
        if city in customer_utterance:
            ie_values_dict["city"] = city
    for day_key, day_val in consult_weather_key_terms.items():
        if day_key in customer_utterance:
            print(day_val, customer_utterance)
            ie_values_dict["date"] = day_val
    return ie_values_dict


def confirm_consult_weather(customer_utterance, confirm_interpreter, senta_gru, city_ls):
    ie_slot_result = ie_city_date(customer_utterance, city_ls)
    if ie_slot_result:
        print("nlu change", ie_slot_result)
        return "change", ie_slot_result
    confirm_state = confirm_nlu.judge_confirm_classification(customer_utterance, senta_gru, confirm_interpreter)
    print(confirm_state)
    return confirm_state, None

