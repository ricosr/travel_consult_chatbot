# -*- coding: utf-8 -*-

from consult.dinning import dinning_handle
from slots.consult_slot import dinning_slot


intent_config = {
    '1b': dinning_handle
}

slot_config = {
    '1b': dinning_slot
}

positive_confirm = ["yes", "sure", "OK", "of course"]

negative_confirm = ["no", "not"]
