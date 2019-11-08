# -*- coding:utf-8 -*-

from random import choice


def ask_city_date():
    response_sentences = [
        "请问您查询哪个城市哪一天的天气？（我们支持国内城市今天、明天、后天的天气查询）\n例如：北京明天天气怎么样？"
    ]
    return choice(response_sentences)


def ask_city():
    response_sentences = [
        "请问您查询哪个城市的天气？\n例如：北京明天天气怎么样？"
    ]
    return choice(response_sentences)


def ask_date():
    response_sentences = [
        "请问您查询哪天的天气？（我们支持国内城市今天、明天、后天的天气查询）\n例如：北京明天天气怎么样？"
    ]
    return choice(response_sentences)


def response_weather_result(weather_info, slot_dict):   # TODO: must
    if not weather_info:
        current_slot_values = ''
        if "city" in slot_dict:
            current_slot_values += "您选择的城市:{}\n".format(slot_dict["city"])
        if "date" in slot_dict:
            day_key_word = {1: "今天", 2: "明天", 3: "后天"}
            current_slot_values += "您选择的日期:{}\n".format(day_key_word[slot_dict["date"]])
        return current_slot_values + "对不起，按照您的要求我没有查询到天气。（我只支持今天，明天和后天的三天查询）"
    return weather_info
