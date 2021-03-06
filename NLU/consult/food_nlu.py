# -*- coding: utf-8 -*-


from slots.consult_slot import consult_food_slot
from NLU.common import confirm_nlu
from NLU.consult.consult_nlu_key_terms import consult_food_key_terms


food_term_tag = ["n", "nz", "PER", "ORG"]
restaurant_term_tag = ["ORG", "an", "nt", "nr", "s", "nw"]
location_term_tag = ["LOC", "ns", "f"]


def judge_all_entities(ie_values_dict):
    if not ie_values_dict:
        return False
    ie_keys = ie_values_dict.keys()
    for slot_key in consult_food_slot.keys():
        if slot_key not in ie_keys:
            return False
    # for ie_key, v in ie_values_dict.items():
    #     if ie_key not in slot_keys:
    #         return False
    return True


def paddle_lac(text, lac):
    lac_inputs = {"text": [text]}
    lac_result_dict = lac.lexical_analysis(data=lac_inputs)[0]
    return lac_result_dict


def ie_all_consult_food(customer_utterance, lac, entities):
    ie_values_dict = {}
    lac_result_dict = paddle_lac(customer_utterance, lac)
    print(3, entities)
    if entities:
        for entity in entities:
            if entity["entity"] == "food":
                ie_values_dict["food"] = entity["value"]
            if entity["entity"] == "destination" or entity["entity"] == "departure":
                entity_lac_results = paddle_lac(entity["value"], lac)
                for tag_index in range(len(entity_lac_results["tag"])):
                    if lac_result_dict["tag"][tag_index] in location_term_tag:
                        ie_values_dict["location"] = entity["value"]
                    else:
                        ie_values_dict["restaurant"] = entity["value"]
            if entity["entity"] == "hotel":
                ie_values_dict["restaurant"] = entity["value"]
    if not judge_all_entities(ie_values_dict):
        print(judge_all_entities(ie_values_dict))
        print(lac_result_dict["tag"])
        if len(lac_result_dict["tag"]) == 1 and lac_result_dict["tag"][0] in food_term_tag:
            ie_values_dict["food"] = customer_utterance
            return ie_values_dict
        if len(lac_result_dict["tag"]) == 1 and lac_result_dict["tag"][0] in restaurant_term_tag:
            ie_values_dict["restaurant"] = customer_utterance
            return ie_values_dict
        for tag_index in range(len(lac_result_dict["tag"])):
            continue_key = False
            if lac_result_dict["tag"][tag_index] in food_term_tag and "food" not in ie_values_dict:
                for eat_term in consult_food_key_terms["eat"]:
                    # if "v" in lac_result_dict["tag"][: tag_index] or "vd" in lac_result_dict["tag"][: tag_index] or "vn" in lac_result_dict["tag"][: tag_index]:
                    if eat_term in lac_result_dict["tag"][: tag_index]:
                        ie_values_dict["food"] = lac_result_dict["word"][tag_index]
                        continue_key = True
                        break
                if lac_result_dict["tag"][tag_index] == "ORG":
                    ie_values_dict["restaurant"] = lac_result_dict["word"][tag_index]
                    continue_key = True
                if continue_key is True:
                    continue
            if lac_result_dict["tag"][tag_index] in restaurant_term_tag and "restaurant" not in ie_values_dict:
                ie_values_dict["restaurant"] = lac_result_dict["word"][tag_index]
                continue_key = True
                if continue_key is True:
                    continue
            if lac_result_dict["tag"][tag_index] in location_term_tag and "location" not in ie_values_dict:
                ie_values_dict["location"] = lac_result_dict["word"][tag_index]
                continue_key = True
                if continue_key is True:
                    continue
    print(4, ie_values_dict)
    return ie_values_dict


# def ie_food(customer_utterance, lac, entities):
#     lac_result_dict = paddle_lac(customer_utterance, lac)
#     for tag_index in range(len(lac_result_dict["tag"])):
#         if lac_result_dict["tag"][tag_index] in food_term_tag:
#             if "v" in lac_result_dict["tag"][: tag_index] or "vd" in lac_result_dict["tag"][: tag_index] or "vn" in lac_result_dict["tag"][: tag_index]:
#                 return lac_result_dict["word"][tag_index]
#
#
# def ie_restaurant(customer_utterance, lac, entities):
#     lac_result_dict = paddle_lac(customer_utterance, lac)
#     for tag_index in range(len(lac_result_dict["tag"])):
#         if lac_result_dict["tag"][tag_index] in restaurant_term_tag:
#             return lac_result_dict["word"][tag_index]
#
#
# def ie_location(customer_utterance, lac, entities):
#     lac_result_dict = paddle_lac(customer_utterance, lac)
#     for tag_index in range(len(lac_result_dict["tag"])):
#         if lac_result_dict["tag"][tag_index] in location_term_tag:
#             return lac_result_dict["word"][tag_index]

def confirm_consult_food(customer_utterance, lac, intent_model, senta_gru, confirm_interpreter):
    intent, entities = intent_model.get_intent(customer_utterance)
    ie_slot_result = ie_all_consult_food(customer_utterance, lac, entities)
    if ie_slot_result:
        return "change", ie_slot_result
    confirm_state = confirm_nlu.judge_confirm_classification(customer_utterance, senta_gru, confirm_interpreter)
    print(confirm_state)
    return confirm_state, None

