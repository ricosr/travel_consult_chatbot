# -*- coding:utf-8 -*-

from NLU.common.confirm_terms import confirm_terms_dict

confidence_threshold = 0.5

yes_intent_threshold = 0.6    # TODO: need to test
no_intent_threshold = 0.6
stop_intent_threshold = 0.6
nothing_intent_threshold = 0.6

yes_positive_threshold = 0.67
no_negative_threshold = 0.79
nothing_negative_threshold = 0.61


def judge_confirm_classification(customer_utterance, senta_gru, confirm_interpreter):
    intent_dict = confirm_interpreter.parse(customer_utterance)
    intent = intent_dict["intent"]["name"]
    confidence = intent_dict["intent"]["confidence"]

    input_dict = {"text": customer_utterance}
    result = senta_gru.sentiment_classify(data=input_dict)[0]
    positive_probs = result['positive_probs']
    negative_probs = result['negative_probs']
    print(6, intent, confidence, positive_probs, negative_probs)

    if confidence < confidence_threshold:
        return "nothing"

    if str(intent) == "yes":
        # if negative_probs > positive_probs:
        #     return "nothing"
        if confidence < yes_intent_threshold:
            if positive_probs > yes_positive_threshold:
                return intent
            else:
                for term in confirm_terms_dict["yes"]:
                    if term in customer_utterance:
                        return intent
                return "nothing"
        else:
            print(intent)
            return intent
    if intent == "no":
        # if negative_probs < positive_probs:
        #     return "nothing"
        if confidence < no_intent_threshold:
            if negative_probs > no_negative_threshold:
                return intent
            else:
                for term in confirm_terms_dict["no"]:
                    if term in customer_utterance:
                        return intent
                return "nothing"
        else:
            return intent
    if intent == "stop":
        # if negative_probs < positive_probs:
        #     return "nothing"
        if confidence < nothing_intent_threshold:
            if negative_probs > nothing_negative_threshold:
                return intent
            else:
                for term in confirm_terms_dict["stop"]:
                    if term in customer_utterance:
                        return intent
                return "nothing"
        else:
            return intent
    if intent == "nothing":
        return intent

