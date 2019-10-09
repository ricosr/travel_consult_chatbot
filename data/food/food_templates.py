# -*- coding: utf-8 -*-

# start0 = 3
# start1 = 3
# start2 = 7
# start3 = 2
# start_0 = 3
# start_1 = 3
# start_2 = 7

food_template = """
- 我想吃[{food}](food)啊
- 找个吃[{food}](food)的店
- 这附近哪里有吃[{food}](food)的地方
- 找个[{food}](food)馆子
- 我想喝[{food}](food)啊
- 找个喝[{food}](food)的店
- 这附近哪里有喝[{food}](food)的地方
- 附近有什么好吃的地方吗
- 肚子饿了，推荐一家吃放的地儿呗
- 带老婆孩子去哪里吃饭比较好
- 想去一家有情调的餐厅
- 我饿了
- 帮我找个吃饭的地方吧
- 我想吃好吃的
- 推荐吃饭的地方
- 哪里有吃饭的地方
- 有什么吃的
- 附近有什么能填饱肚子的地方
- 找个喝水的地方
- 好渴，帮我找个冷饮店
- 我想喝点东西
"""

food_template_ls1 = [
"- 我想吃[{food}](food)",
"- 找个吃[{food}](food)的店",
"- 这附近哪里有吃[{food}](food)的地方",
"- 找个[{food}](food)馆子",
"- 我想喝[{food}](food)啊",
"- 找个喝[{food}](food)的店",
"- 这附近哪里有喝[{food}](food)的地方"]

food_template_ls2 = [
"- 附近有什么好吃的地方吗",
"- 肚子饿了，推荐一家吃放的地儿呗",
"- 带老婆孩子去哪里吃饭比较好",
"- 想去一家有情调的餐厅",
"- 我饿了",
"- 帮我找个吃饭的地方吧",
"- 我想吃好吃的",
"- 推荐吃饭的地方",
"- 哪里有吃饭的地方",
"- 有什么吃的",
"- 附近有什么能填饱肚子的地方",
"- 找个喝水的地方",
"- 好渴，帮我找个冷饮店",
"- 我想喝点东西"
]

# food_template = """
#     {{
#         "text": "我想吃{food}啊",
#         "intent": "food_search",
#         "entities": [
#           {{
#             "start": 3,
#             "end": {end0},
#             "value": "{food}",
#             "entity": "food"
#           }}
#         ]
#     }},
#     {{
#         "text": "找个吃{food}的店",
#         "intent": "food_search",
#         "entities": [
#           {{
#             "start": 3,
#             "end": {end1},
#             "value": "{food}",
#             "entity": "food"
#           }}
#         ]
#     }},
#     {{
#         "text": "这附近哪里有吃{food}的地方",
#         "intent": "food_search",
#         "entities": [
#           {{
#             "start": 7,
#             "end": {end2},
#             "value": "{food}",
#             "entity": "food"
#           }},
#         ]
#     }},
#     {{
#         "text": "找个{food}馆子",
#         "intent": "food_search",
#         "entities": [
#           {{
#             "start": 2,
#             "end": {end3},
#             "value": "{food}",
#             "entity": "food"
#           }}
#         ]
#     }},
#     {{
#         "text": "我想喝{food}啊",
#         "intent": "food_search",
#         "entities": [
#           {{
#             "start": 3,
#             "end": {end_0},
#             "value": "{food}",
#             "entity": "food"
#           }}
#         ]
#     }},
#     {{
#         "text": "找个喝{food}的店",
#         "intent": "food_search",
#         "entities": [
#           {{
#             "start": 3,
#             "end": {end_1},
#             "value": "{food}",
#             "entity": "food"
#           }}
#         ]
#     }},
#     {{
#         "text": "这附近哪里有喝{food}的地方",
#         "intent": "food_search",
#         "entities": [
#           {{
#             "start": 7,
#             "end": {end_2},
#             "value": "{food}",
#             "entity": "food"
#           }},
#         ]
#     }},
#     {{
#         "text": "附近有什么好吃的地方吗",
#         "intent": "food_search",
#         "entities": []
#     }},
#     {{
#         "text": "肚子饿了，推荐一家吃放的地儿呗",
#         "intent": "food_search",
#         "entities": []
#     }},
#     {{
#         "text": "带老婆孩子去哪里吃饭比较好",
#         "intent": "food_search",
#         "entities": []
#     }},
#     {{
#         "text": "想去一家有情调的餐厅",
#         "intent": "food_search",
#         "entities": []
#     }},
#     {{
#         "text": "我饿了",
#         "intent": "food_search",
#         "entities": []
#     }},
#     {{
#         "text": "帮我找个吃饭的地方吧",
#         "intent": "food_search",
#         "entities": []
#     }},
#     {{
#         "text": "我想吃好吃的",
#         "intent": "food_search",
#         "entities": []
#     }},
#     {{
#         "text": "推荐吃饭的地方",
#         "intent": "food_search",
#         "entities": []
#     }},
#     {{
#         "text": "哪里有吃饭的地方",
#         "intent": "food_search",
#         "entities": []
#     }},
#     {{
#         "text": "有什么吃的",
#         "intent": "food_search",
#         "entities": []
#     }},
#     {{
#         "text": "附近有什么能填饱肚子的地方",
#         "intent": "food_search",
#         "entities": []
#     }},
#     {{
#         "text": "找个喝水的地方",
#         "intent": "food_search",
#         "entities": []
#     }},
#     {{
#         "text": "好渴，帮我找个冷饮店",
#         "intent": "food_search",
#         "entities": []
#     }},
#      """
