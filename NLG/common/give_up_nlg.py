# -*- coding:utf-8 -*-

from random import choice

response_sentences = [
    "谢谢！再见！"
]


def robot_response_give_up():
    return choice(response_sentences)