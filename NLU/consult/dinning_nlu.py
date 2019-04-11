# -*- coding: utf-8 -*-

import re
import copy

import nltk

from slots.consult_slot import dinning_slot
from NLU.consult.dinning_rule import rule_1a, rule_2, key_word_3, key_word_4b
from NLU.consult.dinning_rule import positive_confirm_phrase, positive_confirm, negative_confirm


def dinning_nlu_rule(customer_utterance):
    ie_values_dict = {}
    match_obj = re.search(rule_1a, customer_utterance)
    return_key = False
    if match_obj:
        return_key = True
        ie_values_dict["restaurant"] = match_obj.group(1)   # TODO: temp

    match_obj = re.search(rule_2, customer_utterance)
    if match_obj:
        return_key = True
        ie_values_dict["food"] = match_obj.group(2)   # TODO: temp

    for word_3 in key_word_3:
        if word_3 in customer_utterance:
            return_key = True
            ie_values_dict["area"] = word_3
            break

    for word_4b in key_word_4b:
        if word_4b in customer_utterance:
            return_key = True
            ie_values_dict["price"] = word_4b
            break

    if return_key is True:
        return ie_values_dict, None
    
    for phrase in positive_confirm_phrase:    # positive phrase answers
        if phrase in customer_utterance:
            return ie_values_dict, "positive"    # TODO: temp
    utterance_list = nltk.word_tokenize(customer_utterance.lower())
    # print(utterance_list)
    for confirm_p, confirm_n in zip(positive_confirm, negative_confirm):    # positive and negative answer
        for word in utterance_list:
            if confirm_p == word:
                return ie_values_dict, "positive"   # TODO: temp
            if confirm_n == word:
                return ie_values_dict, "negative"   # TODO: temp
    return ie_values_dict, None

