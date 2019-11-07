# -*- coding: utf-8 -*-

from random import choice


def ask_depart_dest_vehicle():  # TODO
    response_sentences = [
        "请问你的出发地，目的地，交通工具是什么\n例如：坐公交从A地去B地怎么走？"
    ]
    return choice(response_sentences)


def ask_depart():
    response_sentences = [
        "请问你的出发地是哪里\n例如：从王府井出发"
    ]
    return choice(response_sentences)


def ask_dest():
    response_sentences = [
        "请问你的目的地是哪里\n例如：到北京西站"
    ]
    return choice(response_sentences)


def ask_vehicle():
    response_sentences = [
        "请问你的交通方式是什么\n例如：打车, 驾车, 公交, 步行, 骑行, 火车, 飞机, 客车, 摩托车"
    ]
    return choice(response_sentences)


def response_traffic_list(search_traffic_results, slot_dict):
    if not search_traffic_results:
        current_slot_values = ''
        if "departure" in slot_dict:
            current_slot_values += "您选择的出发地:{}\n".format(slot_dict["departure"])
        if "destination" in slot_dict:
            current_slot_values += "您选择的目的地:{}\n".format(slot_dict["destination"])
        if "vehicle" in slot_dict:
            current_slot_values += "您选择的出行方式:{}\n".format(slot_dict["vehicle"])
        if "departure_time" in slot_dict:
            if slot_dict["departure_time"] != 0:
                current_slot_values += "您选择的出行时间:{}\n".format(slot_dict["departure_time"])
        return current_slot_values + "抱歉，这个路线我查不到"
    traffic_solutions = []
    for key, route in search_traffic_results.items():
        traffic_solutions.append("{}: {}".format(key, route))
    return '\n'.join(traffic_solutions) + '\n您觉得可以吗？'
