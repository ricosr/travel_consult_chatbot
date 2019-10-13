# -*- coding: utf-8 -*-

from slots.consult_slot import consult_traffic_slot
from NLU.common import confirm_nlu
from nlu_key_terms import search_traffic_key_terms


departure_destination_term_tag = ["LOC", "ORG", "PER", "ns", "nr", "nz", "f", "s", "nt", "nw"]
vehicle_term_tag = ["n", "nz"]
departure_time_term_tag = ["TIME", "m", "q", "t"]


def judge_all_entities(ie_values_dict):
    if not ie_values_dict:
        return False
    slot_keys = consult_traffic_slot.keys()
    for ie_key, v in ie_values_dict.items():
        if ie_key not in slot_keys:
            return False
    return True


def paddle_lac(text, lac):
    lac_inputs = {"text": [text]}
    lac_result_dict = lac.lexical_analysis(data=lac_inputs)[0]
    return lac_result_dict


def convert_to_num(customer_utterance):    # TODO: convert chinese number character into number
    return customer_utterance


def ie_all_search_food(customer_utterance, lac, entities):
    customer_utterance_tmp = convert_to_num(customer_utterance)
    ie_values_dict = {}
    lac_result_dict = paddle_lac(customer_utterance_tmp, lac)
    if entities:
        for entity in entities:
            if entity["entity"] == "departure":
                ie_values_dict["departure"] = entity["value"]
            if entity["entity"] == "destination":
                ie_values_dict["destination"] = entity["value"]
            if entity["entity"] == "hotel":
                ie_values_dict["destination"] = entity["value"]
            if entity["entity"] == "vehicle":
                for vehicle, terms_ls in search_traffic_key_terms["vehicle_terms"].items():
                    for term in terms_ls:
                        if entity["value"] in term or term in entity["value"]:
                            ie_values_dict["vehicle"] = vehicle
                            break
                    if "vehicle" in ie_values_dict:
                        break
    if not judge_all_entities(ie_values_dict):
        if len(lac_result_dict["tag"]) == 1 and lac_result_dict["tag"][0] in departure_destination_term_tag:
            ie_values_dict["destination"] = customer_utterance
        for tag_index in range(len(lac_result_dict["tag"])):
            if lac_result_dict["tag"][tag_index] in departure_destination_term_tag:
                departure_judge = True
                if 'p' in lac_result_dict["tag"][: tag_index]:
                    p_index = lac_result_dict["tag"][: tag_index].index('p')
                    for tag in lac_result_dict["tag"][: tag_index][p_index:]:
                        if tag in departure_destination_term_tag:
                            departure_judge = False
                            break
                    if departure_judge is True:
                        ie_values_dict["departure"] = lac_result_dict["word"][tag_index]
                else:
                    destination_judge = True
                    if 'v' in lac_result_dict["tag"][: tag_index]:
                        v_index = lac_result_dict["tag"][: tag_index].index('v')
                    elif "vd" in lac_result_dict["tag"][: tag_index]:
                        v_index = lac_result_dict["tag"][: tag_index].index("vd")
                    elif "vn" in lac_result_dict["tag"][: tag_index]:
                        v_index = lac_result_dict["tag"][: tag_index].index("vn")
                    else:
                        continue
                    for tag in lac_result_dict["tag"][: tag_index][v_index:]:
                        if tag in departure_destination_term_tag:
                            destination_judge = False
                            break
                    if destination_judge is True:
                        ie_values_dict["destination"] = lac_result_dict["word"][tag_index]
            if lac_result_dict["tag"][tag_index] in vehicle_term_tag:
                # TODO
                pass


def ie_departure_time(customer_utterance, lac, entities):
    pass
