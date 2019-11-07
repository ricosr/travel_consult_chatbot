# -*- coding: utf-8 -*-

from random import choice


def ask_depart_dest_vehicle_date():  # TODO
    response_sentences = [
        "请问您的出发时间，出发城市，目的城市，计划乘坐什么交通工具？\n例如：8月8号坐飞机从北京去上海"
    ]
    return choice(response_sentences)


def ask_depart():
    response_sentences = [
        "请问您的出发城市是哪里？\n例如：从北京出发"
    ]
    return choice(response_sentences)


def ask_dest():
    response_sentences = [
        "请问您的目的城市是哪里？\n例如：到上海"
    ]
    return choice(response_sentences)


def ask_vehicle():
    response_sentences = [
        "请问您的交通方式是什么？\n例如：火车, 飞机, 客车"
    ]
    return choice(response_sentences)


def ask_departure_date():
    response_sentences = [
        "请问您的出发日期是几号？\n例如：2020年1月1日"
    ]
    return choice(response_sentences)


def response_solution_list(search_solution_results, slot_dict):
    if search_solution_results:
        response_text = ''
        for solution_no, solution in search_solution_results.items():
            response_text += "{}: {}\n".format(solution_no, solution)
        return '\n' + response_text + '\n请您在以上方案中选择一个方案的编号（输入 0,1,2,3...）'
    else:
        current_slot_values = ''
        if "departure" in slot_dict:
            current_slot_values += "您选择的出发城市:{}\n".format(slot_dict["departure"])
        if "destination" in slot_dict:
            current_slot_values += "您选择的目的城市:{}\n".format(slot_dict["destination"])
        if "vehicle" in slot_dict:
            current_slot_values += "您选择的出行方式:{}\n".format(slot_dict["vehicle"])
        if "departure_date" in slot_dict:
            current_slot_values += "您选择的出行日期:{}\n".format(slot_dict["departure_date"])
        if "name" in slot_dict:
            current_slot_values += "您的姓名:{}\n".format(slot_dict["name"])
        if "ID" in slot_dict:
            current_slot_values += "您的身份证号码:{}\n".format(slot_dict["ID"])
        return current_slot_values + "抱歉，按照您的要求，我没有查询到结果。"


def ask_name_ID():
    response_sentences = [
        "请问您的姓名和身份证号？\n例如：我叫李小明，身份证号码是110101199101010001"
    ]
    return choice(response_sentences)


def ask_name():
    response_sentences = [
        "请问您的姓名是什么？\n例如：我叫李小明"
    ]
    return choice(response_sentences)


def ask_ID():
    response_sentences = [
        "请问您的身份证号码？\n例如：我的身份证号码是110101199101010001"
    ]
    return choice(response_sentences)


def confirm_ticket_info(confident_slot_values):
    show_current_msg = ''
    show_current_msg += "出发城市：{},\n".format(confident_slot_values["departure"])
    show_current_msg += "目的城市：{},\n".format(confident_slot_values["destination"])
    show_current_msg += "交通方式：{},\n".format(confident_slot_values["vehicle"])
    show_current_msg += "出发日期：{},\n".format(confident_slot_values["departure_date"])
    show_current_msg += "姓名：{},\n".format(confident_slot_values["name"])
    show_current_msg += "身份证号：{},\n".format(confident_slot_values["ID"])
    show_current_msg += "订票序号：{},\n".format(confident_slot_values["solution_no"])

    return "\n请确认票面信息:\n" + show_current_msg + "\n是否确认？"
