# -*- coding: utf-8 -*-

from random import choice


def ask_food_restaurant():  # TODO
    response_sentences = [
        "请问你您想吃什么？或者告诉我饭厅名字。\n例如：我想吃火锅"
    ]
    return choice(response_sentences)


def response_restaurant_list(search_parameters):   # TODO
    restaurant_list = [   # temp
        "餐厅1",
        "餐厅2",
        "餐厅3",
        "餐厅4",
    ]
    return '\n'.join(restaurant_list) + '\n您觉得可以吗？'
