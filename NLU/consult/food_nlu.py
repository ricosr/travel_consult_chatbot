# -*- coding: utf-8 -*-

import re


def search_food_ie(customer_utterance, lac, entities):
    ie_values_dict = {}
    lac_inputs = {"text": customer_utterance}
    lac_result_dict = lac.lexical_analysis(data=lac_inputs)[0]
    food_term_tag = ["n", "nr", "nz", "PER"]
    return_key = False   # if extract value, it is True
    if entities:
        for entity in entities:
            if entity["entity"] == "food":
                ie_values_dict["food"] = entity["value"]
                return_key = True
            if entity["entity"] == "position2" or entity["entity"] == "position1":
                ie_values_dict["restaurant"] = entity["value"]
                return_key = True
    else:
        for tag_index in range(len(lac_result_dict["tag"])):
            if lac_result_dict["tag"][tag_index] in food_term_tag:
                if "v" in lac_result_dict["tag"][: tag_index] or "vd" in lac_result_dict["tag"][: tag_index] or "vn" in lac_result_dict["tag"][: tag_index]:
                    ie_values_dict["food"] = lac_result_dict["word"][tag_index]
                    return_key = True
                    break
    
    



