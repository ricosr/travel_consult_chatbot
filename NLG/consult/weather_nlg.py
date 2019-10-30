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


def response_weather_result(weather_info):   # TODO: must
    return weather_info
