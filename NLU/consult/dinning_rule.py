# -*- coding: utf-8 -*-

import re

rule_1a = re.compile(r'([a-zA-Z0-9]*)(\srestaurant)', re.I)
rule_2 = re.compile(r'([a-zA-Z0-9]*)(\sfood)', re.I)
key_word_3 = ["nearby", "near", "far", "across", "adjacent", "around", "back", "beside", "inside", "in front of", "through"]
key_word_4b = ["expensive", "cheap", "cheap", "cheapest"]

positive_confirm = ["yes", "sure", "ok"]
negative_confirm = ["no", "not", None]

positive_confirm_phrase = ["no problem", "of course"]