# -*- coding: utf-8 -*-

import nltk

from slots.consult_slot import dinning_slot
from config.config import positive_confirm, negative_confirm


def dinning_nlu_rule(customer_utterance):
    utterance_list = nltk.word_tokenize(customer_utterance.lower())
    for confirm_p, confirm_n in zip(positive_confirm, negative_confirm):
        for word in utterance_list:
            if confirm_p == word:
                return dinning_slot, "yes"
            if confirm_n == word:
                return dinning_slot, "no"

