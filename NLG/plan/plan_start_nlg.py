# -*- coding:utf-8 -*-

from random import choice


def ask_start_plan(intent):
    if intent == "plan_ticket":
        response_sentences = ["请问告诉我您的出发地，目的地，交通方式和出发日期\n例如：8月8号从北京去上海，飞机"]
    if intent == "plan_scenic_spot":
        response_sentences = ["请告诉我您的旅游城市和旅行天数\n例如：去北京玩5天"]
    return choice(response_sentences)
    # TODO: add others

