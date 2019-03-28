# -*- coding: utf-8 -*-

from consult.dinning import dinning_handle
from slots.consult_slot import dinning_slot


intent_config = {
    '1b': dinning_handle
}

slot_config = {
    '1b': dinning_slot
}

positive_confirm = ["yes", "sure", "ok"]
positive_confirm_phrase = ["no problem", "of course"]

negative_confirm = ["no", "not"]
