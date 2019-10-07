# -*- coding: utf-8 -*-

import paddlehub as hub


def cal_sum(result_dict):
    tmp_sum={}
    for key, ls in result_dict.items():
        tmp_positive = 0
        tmp_negative = 0
        for each_term in ls:
            tmp_positive += each_term[1]
            tmp_negative += each_term[2]
        tmp_sum[key] = [tmp_positive/len(ls), tmp_negative/len(ls)]
    return (tmp_sum)

yes_ls=["嗯","好的","OK","没问题","行","可以的","可以","恩","嗯","中","办吧","妥了","办理吧","行的","谢了","哦了","欧了","yes","成","稳"]

no_ls=["不是","不行","不对","有问题","我再考虑考虑","不好啦","不行","不可以的","不中","不可以","no","不OK","换一个","改一下","选一选","选一个","改","不好","不成","不妥","不太行","不太对","改条件"]

stop_ls=["不需要","不要办","不办","暂时不要了","不要","算了","算了吧","结束","不找了","不用了","没有了","没了","暂时不用了","好的没了","好不用了","没用了","拉倒吧"]

nothing_ls=["考虑一下","我想想","等等","什么","垃圾","哈哈","呃","没明白","不知道","不懂","啥","啥子","等会","看一下","一下下","瞧一瞧"]

module_name_ls=["senta_lstm", "senta_gru", "senta_cnn", "senta_bow", "senta_bilstm", "emotion_detection_textcnn"]
confirm_name_ls = ["yes", "no", "stop", "nothing"]

with open("test_result.txt", 'w', encoding="utf-8") as fpw:
    for module_name in module_name_ls:
        fpw.write(module_name + ':\n')
        senta = hub.Module(name=module_name)
        i = 0
        tmp_result_dict = {}

        for test_text in [yes_ls, no_ls, stop_ls, nothing_ls]:
            tmp_result_dict[confirm_name_ls[i]] = []
            input_dict = {"text": test_text}
            if module_name == "emotion_detection_textcnn":
                results = senta.emotion_classify(data=input_dict)
            else:
                results = senta.sentiment_classify(data=input_dict)

            for result in results:
                tmp_result_dict[confirm_name_ls[i]].append([result['text'], result['positive_probs'], result['negative_probs']])

            i += 1
        fpw.write(str(tmp_result_dict))
        fpw.write('\n')
        fpw.write(str(cal_sum(tmp_result_dict)))
        fpw.write("\n\n\n")

