# -*- coding: utf-8 -*-

from random import choice


def ask_food_restaurant():
    response_sentences = [
        "请问你您想吃什么？或者告诉我饭厅名字。\n例如：我想吃火锅"
    ]
    return choice(response_sentences)
