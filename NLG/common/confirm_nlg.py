# -*- coding:utf-8 -*-

from random import choice


def response_yes():
    yes_sentences = [
        "谢谢！"
    ]
    return choice(yes_sentences)


def response_no(intent, confident_slot_values):
    show_current_msg = "您现在的需求是："
    no_response_dict = {
        "consult_food": ["\n请问您还有别的要求吗？吃的其他的？换一个餐厅？还是有地点的要求？"],
        "consult_traffic": ["\n请问您还有别的要求吗？更换目的地？出发地？还是交通方式？"]
    }
    if intent == "consult_food":
        if "food" in confident_slot_values:
            show_current_msg += "食物：{},".format(confident_slot_values["food"])
        if "restaurant" in confident_slot_values:
            show_current_msg += "餐厅：{},".format(confident_slot_values["restaurant"])
        if "location" in confident_slot_values:
            show_current_msg += "地点：{},".format(confident_slot_values["location"])

    if intent == "consult_traffic":
        if "departure" in confident_slot_values:
            show_current_msg += "出发地：{},".format(confident_slot_values["departure"])
        if "destination" in confident_slot_values:
            show_current_msg += "目的地：{},".format(confident_slot_values["destination"])
        if "vehicle" in confident_slot_values:
            show_current_msg += "交通方式：{},".format(confident_slot_values["vehicle"])
        if "departure_time" in confident_slot_values:
            show_current_msg += "出发时间：{},".format(confident_slot_values["departure_time"])

    return show_current_msg + choice(no_response_dict[intent])


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