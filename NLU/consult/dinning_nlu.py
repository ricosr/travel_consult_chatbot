# -*- coding: utf-8 -*-

from slots.consult_slot import dinning_slot


def dinning_nlu_rule(customer_utterance):
    return dinning_slot, "yes"
