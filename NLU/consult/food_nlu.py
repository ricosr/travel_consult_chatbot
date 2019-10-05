# -*- coding: utf-8 -*-


from slots.consult_slot import consult_food_slot


food_term_tag = ["n", "nr", "nz", "PER"]
restaurant_term_tag = ["ORG", "an", "nt", "s", "nw"]
location_term_tag = ["LOC", "ns", "f"]


def judge_all_entities(ie_values_dict):
    slot_keys = consult_food_slot.keys()
    for ie_key in ie_values_dict.items():
        if ie_key not in slot_keys:
            return False
    return True


def paddle_lac(text, lac):
    lac_inputs = {"text": [text]}
    lac_result_dict = lac.lexical_analysis(data=lac_inputs)[0]
    return lac_result_dict


def ie_all_search_food(customer_utterance, lac, entities):
    ie_values_dict = {}
    lac_result_dict = paddle_lac(customer_utterance, lac)
    return_key = False   # if extract value, it is True
    if entities:
        for entity in entities:
            if entity["entity"] == "food":
                ie_values_dict["food"] = entity["value"]
                return_key = True
            if entity["entity"] == "position2" or entity["entity"] == "position1":
                entity_lac_results = paddle_lac(entity["value"], lac)
                for tag_index in range(len(entity_lac_results["tag"])):
                    if lac_result_dict["tag"][tag_index] in restaurant_term_tag:
                        ie_values_dict["restaurant"] = entity["value"]
                        return_key = True
                    if lac_result_dict["tag"][tag_index] in location_term_tag:
                        ie_values_dict["location"] = entity["value"]
                        return_key = True
    if not judge_all_entities(ie_values_dict):
        for tag_index in range(len(lac_result_dict["tag"])):
            if lac_result_dict["tag"][tag_index] in food_term_tag:
                if "v" in lac_result_dict["tag"][: tag_index] or "vd" in lac_result_dict["tag"][: tag_index] or "vn" in lac_result_dict["tag"][: tag_index]:
                    ie_values_dict["food"] = lac_result_dict["word"][tag_index]
                    return_key = True
            if lac_result_dict["tag"][tag_index] in restaurant_term_tag:
                ie_values_dict["restaurant"] = lac_result_dict["word"][tag_index]
                return_key = True
            if lac_result_dict["tag"][tag_index] in location_term_tag:
                ie_values_dict["location"] = lac_result_dict["word"][tag_index]
                return_key = True
    return ie_values_dict


def ie_food(customer_utterance, lac, entities):
    lac_result_dict = paddle_lac(customer_utterance, lac)
    for tag_index in range(len(lac_result_dict["tag"])):
        if lac_result_dict["tag"][tag_index] in food_term_tag:
            if "v" in lac_result_dict["tag"][: tag_index] or "vd" in lac_result_dict["tag"][: tag_index] or "vn" in lac_result_dict["tag"][: tag_index]:
                return lac_result_dict["word"][tag_index]


def ie_restaurant(customer_utterance, lac, entities):
    lac_result_dict = paddle_lac(customer_utterance, lac)
    for tag_index in range(len(lac_result_dict["tag"])):
        if lac_result_dict["tag"][tag_index] in restaurant_term_tag:
            return lac_result_dict["word"][tag_index]


def ie_location(customer_utterance, lac, entities):
    lac_result_dict = paddle_lac(customer_utterance, lac)
    for tag_index in range(len(lac_result_dict["tag"])):
        if lac_result_dict["tag"][tag_index] in location_term_tag:
            return lac_result_dict["word"][tag_index]
