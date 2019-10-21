# -*- coding:utf-8 -*-

from random import choice


def ask_start_plan(intent):
    if intent == "plan_ticket":
        response_sentences = ["请问告诉我您的出发地，目的地，交通方式和出发日期\n例如：从北京去上海，飞机"]
        return choice(response_sentences)
    # TODO: add others

