# -*- coding: utf-8 -*-

from random import choice


def ask_food_restaurant():  # TODO
    response_sentences = [
        "请问你您想吃什么？或者告诉我饭厅名字。\n例如：我想吃火锅"
    ]
    return choice(response_sentences)


def response_restaurant_list(restaurant_list):   # TODO
    if restaurant_list:
        result_ls = []
        for restaurant in restaurant_list:
            tmp_result = ''
            for key, info in restaurant.items():
                if key == "_id":
                    continue
                tmp_result += "{}: {}\n".format(key, info)
            result_ls.append(tmp_result)
        return '\n\n'.join(restaurant_list) + '\n\n您觉得可以吗？'
    else:
        return "抱歉，按照您的要求没有查询到结果，请重新输入新的查询条件，或者结束对话，谢谢！"
