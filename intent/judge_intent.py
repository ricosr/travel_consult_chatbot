# -*- coding: utf-8 -*-

from rasa.nlu.model import Interpreter

from intent_temrs import intent_terms_dict


class Intent:
    def __init__(self, model_name='models1'):
        self.interpreter = Interpreter.load("intent/{}/nlu".format(model_name))
        self.threshold = 0.7   # TODO: need to test

    def get_intent(self, utterance):
        intent_dict = self.interpreter.parse(utterance)
        intent = intent_dict["intent"]["name"]
        confidence = intent_dict["intent"]["confidence"]
        if confidence < self.threshold:
            for intent, terms_ls in intent_terms_dict.items():
                for term in terms_ls:
                    if term in utterance:
                        return intent, False
        for entity in intent_dict["entities"]:
            if entity["entity"] == "food":
                intent = "search_food"
        return intent, intent_dict["entities"]

