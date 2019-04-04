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


# [{'_id': ObjectId('5c9dd1ad30736e2180a10911'), 'restaurant': 'kfc', 'food': 'hamburger', 'area': 'near', 'price': 'cheap'}, {'_id': ObjectId('5c9dd1ad30736e2180a10912'), 'restaurant': 'yoshinoya', 'food': 'rice', 'area': 'far', 'price': 'cheap'}, {'_id': ObjectId('5c9dd1ae30736e2180a10913'), 'restaurant': 'abcd', 'food': 'hotpot', 'area': 'near', 'price': 'expensive'}, {'_id': ObjectId('5c9dd23c30736e315896f669'), 'restaurant': 'kfc', 'food': 'hamburger', 'area': 'far', 'price': 'cheap'}]
def nlg_chose_restaurant(restaurant_ls, if_case_no):
    print(restaurant_ls)
    response_sentence = "I find these restaurants according to your requirements:\n"
    if if_case_no == -1:
        response_sentence = "I will find some good restaurants for you randomly:\n"
    for restaurant in restaurant_ls:
        response_sentence += '\trestaurant {}, has {}, in a {} place, average price is {}.\n'.format(restaurant["restaurant"], restaurant["food"], restaurant["area"], restaurant["price"])
    return response_sentence

