# -*- coding:utf-8 -*-

from NLU.common.confirm_nlu import judge_confirm_classification

nothing_intent_threshold = 0.6
nothing_negative_threshold = 0.61


def whether_give_up(customer_utterance, senta_gru, confirm_interpreter):
    intent = judge_confirm_classification(customer_utterance, senta_gru, confirm_interpreter)
    print("whether_give_up", intent)
    if intent == "no" or intent == "stop":
        return True
    else:
        return False

    # intent_dict = confirm_interpreter.parse(customer_utterance)
    # intent = intent_dict["intent"]["name"]
    # confidence = intent_dict["intent"]["confidence"]
    #
    # input_dict = {"text": customer_utterance}
    # result = senta_gru.sentiment_classify(data=input_dict)[0]
    # positive_probs = result['positive_probs']
    # negative_probs = result['negative_probs']
    # if intent is "stop":
    #     return True
    # else:
    #     if negative_probs < positive_probs:
    #         return False
    #     if confidence < nothing_intent_threshold:
    #         if negative_probs > nothing_negative_threshold:
    #             return True
    #         else:
    #             for term in confirm_terms_dict["stop"]:
    #                 if term in customer_utterance:
    #                     return True
    #             return False
    #     else:
    #         return True