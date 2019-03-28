# -*- coding: utf-8 -*-

import nltk

from slots.consult_slot import dinning_slot
from config.config import positive_confirm, negative_confirm, positive_confirm_phrase


def dinning_nlu_rule(customer_utterance):
    for phrase in positive_confirm_phrase:
        if phrase in customer_utterance:
            return dinning_slot, "yes"    # TODO: temp
    utterance_list = nltk.word_tokenize(customer_utterance.lower())
    for confirm_p, confirm_n in zip(positive_confirm, negative_confirm):
        for word in utterance_list:
            if confirm_p == word:
                return dinning_slot, "yes"   # TODO: temp
            if confirm_n == word:
                return dinning_slot, "no"   # TODO: temp

