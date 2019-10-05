# -*- coding:utf-8 -*-

from random import choice


def response_yes():
    yes_sentences = [
        "谢谢！"
    ]
    return choice(yes_sentences)


def response_no():
    no_response = [
        "请问您还有别的要求吗？吃的其他的？换一个餐厅？还是有地点的要求？"
    ]
    return choice(no_response)


def response_give_up():
    stop_sentences = [
        "谢谢！再见！"
    ]
    return choice(stop_sentences)


def response_nothing():
    stop_sentences = [
        "请告诉我 可以 或 不可以，您也可以更改需求，谢谢！"
    ]
    return choice(stop_sentences)