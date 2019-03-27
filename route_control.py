# -*- coding: utf-8 -*-

from intent import judge_intent
from config.config import intent_config

def get_input():
    pass


def response():
    pass


def distribute_task():
    pass


def control():
    print("<<<Can I help you?")
    while True:
        customer_utterance = input(">>>")
        intent = judge_intent.judge_intent()
        handle_function = intent_config[intent]
        print(handle_function())

control()