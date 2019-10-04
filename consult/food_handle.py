# -*- coding:utf-8 -*-

from NLU.consult import food_nlu
from NLU.common import give_up, yes_or_no


def search_food_handle(current_slot, customer_utterance, state_tracker_obj, db_obj, collection_name):
    last_slot_state = state_tracker_obj.get_last_slot_state()
    """if last_slot_state...:
        yes_or_no(customer_utterance)
    else:
        go on"""