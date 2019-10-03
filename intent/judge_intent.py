# -*- coding: utf-8 -*-

from rasa.nlu.model import Interpreter

from intent_temrs import intent_terms_dict


class Intent:
    def __init__(self, model_name='models1'):
        self.interpreter = Interpreter.load("{}/nlu".format(model_name))

    def get_intent(self, utterance):
        intent_dict = self.interpreter.parse(utterance)
        intent = intent_dict["intent"]["name"]
        confidence = intent_dict["intent"]["confidence"]
        if confidence < 0.5:
            for intent, terms_ls in intent_terms_dict.items():
                for term in terms_ls:
                    if term in utterance:
                        return intent, False
        return intent, intent_dict["entities"][0]

