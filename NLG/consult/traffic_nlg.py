# -*- coding: utf-8 -*-

from random import choice


def ask_depart_dest_vehicle():  # TODO
    response_sentences = [
        "请问你的出发地，目的地，交通工具是什么\n例如：坐公交从A地去B地怎么走？"
    ]
    return choice(response_sentences)


def ask_depart():
    response_sentences = [
        "请问你的出发地是哪里\n例如：从王府井出发"
    ]
    return choice(response_sentences)


def ask_dest():
    response_sentences = [
        "请问你的目的地是哪里\n例如：到北京西站"
    ]
    return choice(response_sentences)


def ask_vehicle():
    response_sentences = [
        "请问你的交通方式是什么\n例如：打车, 驾车, 公交, 步行, 骑行, 火车, 飞机, 客车, 摩托车"
    ]
    return choice(response_sentences)


def response_traffic_list(search_traffic_results):
    traffic_solutions = []
    for key, route in search_traffic_results.items():
        traffic_solutions.append("{}: {}".format(key, route))
    return '\n'.join(traffic_solutions) + '\n您觉得可以吗？'
