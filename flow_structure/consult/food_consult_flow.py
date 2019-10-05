# -*- coding:utf-8 -*-

from NLU.consult import food_nlu
from NLU.common import yes_or_no_nlu
from NLU.common import give_up_nlu

from NLG.consult import food_nlg
from NLG.common import yes_or_no_nlg
from NLG.common import give_up_nlg


def consult_food_handle(current_slot, customer_utterance, state_tracker_obj, entities, lac, db_obj, collection_name):
    last_slot_state = state_tracker_obj.get_last_slot_state()

    if not last_slot_state:
        give_up_state = give_up_nlu.whether_give_up(customer_utterance)
        if not give_up_state:
            return give_up_nlg.robot_response_give_up(), "stop"
    else:
        ie_slot_result = food_nlu.ie_all_search_food(customer_utterance, lac, entities)
