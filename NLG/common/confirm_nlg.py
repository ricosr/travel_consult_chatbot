# -*- coding:utf-8 -*-

from random import choice


def response_yes():
    yes_sentences = [
        "谢谢！"
    ]
    return choice(yes_sentences)


def response_no(intent, confident_slot_values):
    show_current_msg = "您现在的需求是：\n"
    no_response_dict = {
        "consult_food": ["\n请问您还有别的要求吗？吃的其他的？换一个餐厅？还是有地点的要求？"],
        "consult_traffic": ["\n请问您还有别的要求吗？更换目的地？出发地？还是交通方式？"],
        "plan_ticket": ["\n请问您还有别的要求吗？更换出发城市？目的城市？交通方式？还是出发日期？"],
        "plan_scenic_spot": ["\n请问您还有别的需求吗？更换旅游城市？还是调整旅游天数？"]
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

    if intent == "plan_ticket":
        if "departure" in confident_slot_values:
            show_current_msg += "出发城市：{},\n".format(confident_slot_values["departure"])
        if "destination" in confident_slot_values:
            show_current_msg += "目的城市：{},\n".format(confident_slot_values["destination"])
        if "vehicle" in confident_slot_values:
            show_current_msg += "交通方式：{},\n".format(confident_slot_values["vehicle"])
        if "departure_time" in confident_slot_values:
            show_current_msg += "出发日期：{},\n".format(confident_slot_values["departure_date"])
        if "name " in confident_slot_values:
            show_current_msg += "姓名：{},\n".format(confident_slot_values["name"])
        if "ID" in confident_slot_values:
            show_current_msg += "身份证号：{},\n".format(confident_slot_values["ID"])
        if "solution_no" in confident_slot_values:
            show_current_msg += "订票序号：{},\n".format(confident_slot_values["solution_no"])

    if intent == "plan_scenic_spot":
        if "city" in confident_slot_values:
            show_current_msg += "旅游城市：{},\n".format(confident_slot_values["departure"])
        if "days" in confident_slot_values:
            show_current_msg += "旅游天数：{},\n".format(confident_slot_values["destination"])
    return show_current_msg + choice(no_response_dict[intent])


def response_give_up():
    stop_sentences = [
        "谢谢！再见！"
    ]
    return choice(stop_sentences)


def response_nothing():
    stop_sentences = [
        "请告诉我 可以 或 不可以，或者直接输入 新的需求，谢谢！"
    ]
    return choice(stop_sentences)
