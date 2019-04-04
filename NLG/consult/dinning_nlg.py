# -*- coding: utf-8 -*-


reply_dict = {
    0: ["Do you prefer some specific restaurant?"],
    1: ["Do you prefer some specific food?"],
    2: ["Do you have demand about the distance from the restaurant?"],
    3: ["Do you have requirement about the average price?"]
}

confirm_dict = {

}


def nlg_confirm_conditions(current_slot):
    response_sentence_ls = ["Do you want ", "a restaurant {}, ", "to eat {}, ", "in {} place, ", "{} price"]
    if current_slot["restaurant"] and current_slot["restaurant"] != "no":
        response_sentence_ls[1] = response_sentence_ls[1].format(current_slot["restaurant"])
    else:
        response_sentence_ls[1] = ''
    if current_slot["food"] != 0 and current_slot["food"] != "no":
        response_sentence_ls[2] = response_sentence_ls[2].format(current_slot["food"])
    else:
        response_sentence_ls[2] = ''
    if current_slot["area"] != 0 and current_slot["area"] != "no":
        response_sentence_ls[3] = response_sentence_ls[3].format(current_slot["area"])
    else:
        response_sentence_ls[3] = ''
    if current_slot["price"] != 0 and current_slot["price"] != "no":
        response_sentence_ls[4] = response_sentence_ls[4].format(current_slot["price"])
    else:
        response_sentence_ls[4] = ''
    return ''.join(response_sentence_ls).strip().rstrip(',') + '?'


def nlg_chose_restaurant(restaurant_ls, if_case_no):
    response_sentence = "I find these restaurants according to your requirements:\n"
    if if_case_no == -1:
        response_sentence = "I will find some good restaurants for you randomly:\n"
    for restaurant in restaurant_ls:
        response_sentence += '\t{}\n'.format(restaurant)
    return response_sentence

