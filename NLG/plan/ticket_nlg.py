# -*- coding: utf-8 -*-

from random import choice


def ask_depart_dest_vehicle():  # TODO
    response_sentences = [
        "请问你的出发城市，目的城市，计划乘坐什么交通工具？\n例如：坐飞机从北京去上海"
    ]
    return choice(response_sentences)


def ask_depart():
    response_sentences = [
        "请问你的出发城市是哪里\n例如：从北京出发"
    ]
    return choice(response_sentences)


def ask_dest():
    response_sentences = [
        "请问你的目的城市是哪里\n例如：到上海"
    ]
    return choice(response_sentences)


def ask_vehicle():
    response_sentences = [
        "请问你的交通方式是什么\n例如：火车, 飞机, 客车"
    ]
    return choice(response_sentences)


# def response_traffic_list(search_parameters):   # TODO
#     traffic_solutions = [   # temp
#         "线路1",
#         "线路2",
#         "线路3",
#         "线路4"
#     ]
#     return '\n'.join(traffic_solutions) + '\n您觉得可以吗？'
