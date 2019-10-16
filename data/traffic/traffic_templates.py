# -*- coding:utf-8 -*-

traffic_template1 = """
- [{destination}](destination)在哪边
- [{destination}](destination)怎么过去啊
- 那个[{destination}](destination)在哪儿啊
- 到[{destination}](destination)怎么走啊
- 这能到[{destination}](destination)
- 请问[{destination}](destination)怎么走
- 那个[{destination}](destination)在什么地方
- 你知道[{destination}](destination)在哪儿吗
- 请问[{destination}](destination)在哪里啊
- 到[{destination}](destination)怎么走
- 我想去[{destination}](destination)
- 帮我找一条路去[{destination}](destination)
- 坐什么能到[{destination}](destination)
- 去[{destination}](destination)怎么坐车
- 帮我找一条线路
- 帮我计划一下路线
- 帮我找一个交通方式
- 计划路线
- 规划路线
"""

traffic_template2 = """
- 从[{departure}](departure)到[{destination}](destination)怎么走
- 在[{departure}](departure)怎么去[{destination}](destination)
- 我想从[{departure}](departure)去[{destination}](destination)怎么办
- 从[{departure}](departure)到[{destination}](destination)[{vehicle}](vehicle)怎么走
- 在[{departure}](departure)[{vehicle}](vehicle)怎么去[{destination}](destination)
- 我想[{vehicle}](vehicle)从[{departure}](departure)去[{destination}](destination)怎么办
"""

traffic_template_ls_1a = [
    "- [{departure}](departure)出发",
    "- 从[{departure}](departure)出发",
    "- 从[{departure}](departure)走",
    "- 从[{departure}](departure)过去",
    "- 出发地是[{departure}](departure)",
    "- 出发是[{departure}](departure)",
    "- 目的地是[{destination}](destination)",
    "- [{destination}](destination)在哪边",
    "- [{destination}](destination)怎么过去啊",
    "- 到[{destination}](destination)怎么走啊",
    "- 这能到[{destination}](destination)",
    "- 请问[{destination}](destination)怎么走",
    "- 那个[{destination}](destination)在什么地方",
    "- 你知道[{destination}](destination)在哪儿吗",
    "- 到[{destination}](destination)怎么走",
    "- 我想去[{destination}](destination)",
    "- 帮我找一条路去[{destination}](destination)",
    "- 坐什么能到[{destination}](destination)",
    "- 去[{destination}](destination)怎么坐车",
    "- [{vehicle}](vehicle)怎么去[{destination}](destination)",
    "- [{vehicle}](vehicle)到[{destination}](destination)怎么走",
    "- [{vehicle}](vehicle)去[{destination}](destination)"
]

traffic_template_ls_1b = [
    "- 从[{departure}](departure)到[{destination}](destination)怎么走",
    "- 在[{departure}](departure)怎么去[{destination}](destination)",
    "- 我想从[{departure}](departure)去[{destination}](destination)怎么办",
    "- 从[{departure}](departure)到[{destination}](destination)[{vehicle}](vehicle)怎么走",
    "- 在[{departure}](departure)[{vehicle}](vehicle)怎么去[{destination}](destination)",
    "- 我想[{vehicle}](vehicle)从[{departure}](departure)去[{destination}](destination)怎么办"
]

traffic_template_ls2 = [
    "- 帮我找一条线路",
    "- 帮我计划一下路线",
    "- 帮我找一个交通方式",
    "- 计划路线",
    "- 规划路线",
    "- 出行规划",
    "- 我要出行",
    "- 我要出门",
    "- 出门",
    "- 出行",
    "- 交通",
    "- 路线"
    "- 找路",
]