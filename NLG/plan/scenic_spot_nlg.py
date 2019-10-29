# -*- coding: utf-8 -*-

from random import choice


def ask_city_days():     # TODO
    response_sentences = [
        "请问您的旅游城市是什么？计划玩几天？（我们暂时只支持小于7天的推荐）\n例如：去北京玩5天"
    ]
    return choice(response_sentences)


def ask_city():
    response_sentences = [
        "请问您的旅游城市是什么？\n例如：去北京玩"
    ]
    return choice(response_sentences)


def ask_days():
    response_sentences = [
        "请问您计划玩几天？（我们暂时只支持小于7天的推荐）\n例如：玩5天"
    ]
    return choice(response_sentences)


def response_scheme_list(search_sheme_results):
    response_text = ''
    for scheme_no, scheme in search_sheme_results.items():
        response_text += "{}: {}\n".format(scheme_no, scheme)
    return '\n' + response_text + '\n请您在以上方案中选择一个方案的编号（输入 1,2,3...）'
