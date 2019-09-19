from stanfordcorenlp import StanfordCoreNLP
with StanfordCoreNLP(r'stanford-corenlp-full-2018-02-27', lang='zh') as zh_model:

    import time
    print(time.time())
    s_zh = '这附近哪里有吃烤串的地方'
    ner_zh = zh_model.ner(s_zh)
    print(time.time())
    s_zh1 = '80%的可能我要从北京去深圳！'
    ner_zh1 = zh_model.ner(s_zh1)
    print(time.time())
    s_zh2 = '万科城到华为坂田基地怎么走？'
    ner_zh2 = zh_model.ner(s_zh2)
    print(ner_zh)
    print(ner_zh1)
    print(ner_zh2)

    print(time.time())