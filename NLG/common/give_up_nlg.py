# -*- coding:utf-8 -*-

# this is on the top of work flow, which may be different from the give-up of step confirm

from random import choice

response_sentences = [
    "谢谢！再见！"
]


def response_give_up():
    return choice(response_sentences)