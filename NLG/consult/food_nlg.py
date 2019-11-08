# -*- coding: utf-8 -*-

from random import choice


def ask_food_restaurant():  # TODO
    response_sentences = [
        "请问你您想吃什么？或者告诉我饭厅名字。\n例如：我想吃火锅"
    ]
    return choice(response_sentences)


def response_restaurant_list(restaurant_list, slot_dict):   # TODO
    if restaurant_list:
        result_ls = []
        for restaurant in restaurant_list:
            tmp_result = ''
            for key, info in restaurant.items():
                if key == "_id":
                    continue
                tmp_result += "{}: {}\n".format(key, info)
            result_ls.append(tmp_result)
        return '\n\n'.join(result_ls) + '\n\n您觉得可以吗？'
    else:
        current_slot_values = ''
        if "food" in slot_dict:
            current_slot_values += "您选择的食物:{}\n".format(slot_dict["food"])
        if "restaurant" in slot_dict:
            current_slot_values += "您选择的餐厅:{}\n".format(slot_dict["restaurant"])
        if "location" in slot_dict:
            current_slot_values += "您选择的地点:{}\n".format(slot_dict["location"])
        return current_slot_values + "抱歉，按照您的要求没有查询到结果，请重新输入新的查询条件，或者结束对话，谢谢！"
