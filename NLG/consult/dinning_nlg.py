# -*- coding: utf-8 -*-

from random import choice


def nlg_confirm_conditions(current_slot):
    judge_key = False
    response_list = [["Do you want ", "a restaurant {}, ", "to eat {}, ", "in {} place, ", "{} price"],
                     ["Again, ", "a restaurant {},", " you can taste {}, ", "and for you {} here, ", "with a {} price, OK?"]
                     ]
    response_sentence_ls = choice(response_list)
    if current_slot["restaurant"] and current_slot["restaurant"] != "no":
        judge_key = True
        response_sentence_ls[1] = response_sentence_ls[1].format(current_slot["restaurant"])
    else:
        response_sentence_ls[1] = ''
    if current_slot["food"] != 0 and current_slot["food"] != "no":
        judge_key = True
        response_sentence_ls[2] = response_sentence_ls[2].format(current_slot["food"])
    else:
        response_sentence_ls[2] = ''
    if current_slot["area"] != 0 and current_slot["area"] != "no":
        judge_key = True
        response_sentence_ls[3] = response_sentence_ls[3].format(current_slot["area"])
    else:
        response_sentence_ls[3] = ''
    if current_slot["price"] != 0 and current_slot["price"] != "no":
        judge_key = True
        response_sentence_ls[4] = response_sentence_ls[4].format(current_slot["price"])
    else:
        response_sentence_ls[4] = ''
    if judge_key:
        return ''.join(response_sentence_ls).strip().rstrip(',') + '?'
    else:
        confirm_1_2 = ["Sorry, you should tell me what do you want to eat or a restaurant?",
                       "Hey, what would you like, food or restaurant?",
                       "Do you mean a kind of food or a name of restaurant?"]
        return choice(confirm_1_2)


# [{'_id': ObjectId('5c9dd1ad30736e2180a10911'), 'restaurant': 'kfc', 'food': 'hamburger', 'area': 'near', 'price': 'cheap'}, {'_id': ObjectId('5c9dd1ad30736e2180a10912'), 'restaurant': 'yoshinoya', 'food': 'rice', 'area': 'far', 'price': 'cheap'}, {'_id': ObjectId('5c9dd1ae30736e2180a10913'), 'restaurant': 'abcd', 'food': 'hotpot', 'area': 'near', 'price': 'expensive'}, {'_id': ObjectId('5c9dd23c30736e315896f669'), 'restaurant': 'kfc', 'food': 'hamburger', 'area': 'far', 'price': 'cheap'}]
def nlg_recommend_restaurant(restaurant_ls, if_case_no):
    response_sentence = "I find these restaurants according to your requirements:\n"
    if if_case_no == -1:
        response_rand_sentence_ls = ["I will find some good restaurants for you randomly:\n",
                                     "I recommend them for you:\n", "These restaurants are recommended for you:\n"]
        response_sentence = choice(response_rand_sentence_ls)
    for restaurant in restaurant_ls:
        response_sentence += '\trestaurant {}, has {}, in a {} place, average price is {}.\n'.format(restaurant["restaurant"], restaurant["food"], restaurant["area"], restaurant["price"])
    return response_sentence


def nlg_confirm_each_slot(slot_key, slot_value):
    confirm_dict = {
        "restaurant": ["Are you sure you want to go to {}?", "Please confirm that you would like to go to {} Y/N",
                       "So, my record shows that you would like to go to {}, it that right?",
                       "Again, i believe that you want to go to {}, ok?"],
        "food": ["Are you sure you want to eat {}?", "Please confirm that you would like to eat {} Y/N",
                 "So, my record shows that you would like to eat{}, it that right?",
                 "Again, i believe that you want to eat{}, ok?"],
        "area": ["Are you sure you prefer a {} place?", "Please confirm that you would like a {} place Y/N",
                 "So, my record shows that you would like a {} place, it that right?",
                 "Again, i believe that you want a {} place, ok?"],
        "price": ["Are you sure you prefer a {} price?", "Please confirm that you would like {} price Y/N",
                  "So, my record shows that you would like price {}, it that right?",
                  "Again, i believe that you want price {}, ok?"]
    }
    confirm_sentence = choice(confirm_dict[slot_key])
    return confirm_sentence.format(slot_value)    # temp TODO: random


def dinning_reply(state_tracker_obj, current_slot):
    reply_dict = {
        "restaurant": ["Do you prefer a specific restaurant?", "You mean a specific restaurant, right?",
                       "So, you would like a specific restaurant, right?"],
        "food": ["Do you prefer some specific food?", "You mean a specific food, right?",
                 "So, you would like a specific food, right?", "What would you like"],
        "area": ["Do you have demand about the distance from the restaurant?", "Should i limit the distance?",
                 "Can you give me a distance range of a restaurant?"],
        "price": ["Do you have requirement about the average price?", "What do you think about the valid price?",
                  "How much do you think is valid price?"]
    }
    for key, value in current_slot.items():
        if not value or value == 0:
            if key in state_tracker_obj.get_state():
                if state_tracker_obj.get_state()[key] == 0:
                    reply_sentence = choice(reply_dict[key])
                    return reply_sentence, key
            else:
                reply_sentence = choice(reply_dict[key])
                return reply_sentence, key
    return None, None


