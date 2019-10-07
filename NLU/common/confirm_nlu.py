# -*- coding:utf-8 -*-


def judge_confirm_classification(customer_utterance, senta_gru, confirm_interp_model):
    if customer_utterance == 0:
        return False
    else:
        return True


