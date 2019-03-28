# -*- coding: utf-8 -*-


def nlg_confirm_conditions(current_slot):
    response_sentence_ls = ["Do you want ", "a restaurant {}, ", "eat {}, ", "in {} place, ", "{} price"]
    if current_slot["restaurant"]:
        response_sentence_ls[1] = response_sentence_ls[1].format(current_slot["restaurant"])
    if current_slot["food_drink"]:
        response_sentence_ls[2] = response_sentence_ls[1].format(current_slot["food_drink"])
    if current_slot["area"]:
        response_sentence_ls[3] = response_sentence_ls[1].format(current_slot["area"])
    if current_slot["price"]:
        response_sentence_ls[4] = response_sentence_ls[1].format(current_slot["price"])
    return ''.join(response_sentence_ls).rstrip(',') + '?'


def nlg_chose_restaurant(restaurant_ls):
    response_sentence = "I find these restaurants according to your requirements:\n"
    for restaurant in restaurant_ls:
        response_sentence += '\t{}\n'.format(restaurant)
    return response_sentence

