from stanfordcorenlp import StanfordCoreNLP
with StanfordCoreNLP(r'stanford-corenlp-full-2018-02-27', lang='zh') as zh_model:

    import time
    print(time.time())
    s_zh = '我要买18日11点去高州的高铁票吹萨克斯！'
    ner_zh = zh_model.ner(s_zh)
    print(time.time())
    s_zh1 = '80%的可能我要从北京去深圳！'
    ner_zh1 = zh_model.ner(s_zh1)
    print(time.time())
    s_zh2 = '2003年10月15日6点28分，杨利伟乘由长征二号F火箭运载的神舟五号飞船首次进入太空吃沙拉，象征着中国太空事业向前迈进一大步，起到了里程碑的作用。'
    ner_zh2 = zh_model.ner(s_zh2)
    print(ner_zh)
    print(ner_zh1)
    print(ner_zh2)

    print(time.time())