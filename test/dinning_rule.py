# -*- coding: utf-8 -*-

import re

rule_1a = re.compile(r'([a-zA-Z0-9]*)(\srestaurant.*)', re.I)  # 定义一个词性list，搭配正则，匹配正则前面的词，按词性列表顺序比对
rule_1a_tag_tuple = (("VB", "VBD", "VBG", "VBN", "VBP", "VBZ"), ("JJ", "JJR", "JJS", "CC", "CD", "DT", "PDT", "WDT", "WP"))

rule_2 = re.compile(r'(eat\s)([a-zA-Z0-9]*)', re.I)
key_word_3 = ["nearby", "near", "far", "across", "adjacent", "around", "back", "beside", "inside", "in front of", "through"]
key_word_4b = ["expensive", "cheap", "cheap", "cheapest"]

positive_confirm = ["yes", "sure", "ok", "right"]
negative_confirm = ["no", "not", "nothing", None]

positive_confirm_phrase = ["no problem", "of course"]