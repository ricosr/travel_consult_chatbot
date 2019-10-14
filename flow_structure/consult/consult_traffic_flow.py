# -*- coding:utf-8 -*-

# intent: search_traffic

from NLU.consult import traffic_nlu
from NLU.common import give_up_nlu

# from NLG.consult import traffic_nlg
from NLG.common import confirm_nlg
from NLG.common import give_up_nlg

from slots.consult_slot import consult_traffic_slot


def consult_traffic_handle(customer_utterance, state_tracker_obj, entities, lac, intent_model, senta_gru, confirm_interpreter, db_obj, collection_name):

    def common_traffic_flow(customer_utterance, state_tracker_obj, entities, lac, db_obj, collection_name):
        give_up_state = give_up_nlu.whether_give_up(customer_utterance, senta_gru, confirm_interpreter)
        if give_up_state:
            state_tracker_obj.update_last_slot_state("stop")
            return give_up_nlg.response_give_up(), "stop"
        else:
            pass    # TODO

    last_slot_state = state_tracker_obj.get_last_slot_state()
    if last_slot_state != "confirm":
        return common_traffic_flow(customer_utterance, state_tracker_obj, entities, lac, db_obj, collection_name)
    else:
        pass    # TODO
