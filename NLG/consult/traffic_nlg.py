# -*- coding: utf-8 -*-

from random import choice


def ask_depart_dest_vehicle():  # TODO
    response_sentences = [
        "请问你的出发地，目的地，交通工具是什么\n例如：坐公交从A地去B地怎么走？"
    ]
    return choice(response_sentences)


def response_restaurant_list(search_parameters):   # TODO
    traffic_solutions = [   # temp
        "线路1",
        "线路2",
        "线路3",
        "线路4"
    ]
    return '\n'.join(traffic_solutions) + '\n您觉得可以吗？'