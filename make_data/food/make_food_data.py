# -*- coding: utf-8 -*-

from food_templates import *


def clean_food_data1(term_file):
    with open(term_file, 'r', encoding="utf-8") as fpr:
        terms_temp_ls = fpr.readlines()
    # terms_ls = [term.split(',')[0] for term in terms_temp_ls]
    terms_ls = [term.strip() for term in terms_temp_ls]
    return terms_ls


def create_food_data(term_file, output_file):
    terms_ls = []
    terms_ls.extend(clean_food_data1(term_file))
    temp_result = ''
    for food_term in terms_ls:
        # temp_result += food_template.format(food=food_term, end0=start0+len(food_term), end1=start1+len(food_term),
        #                                     end2=start2+len(food_term), end3=start3+len(food_term),
        #                                     end_0=start_0+len(food_term), end_1=start_1+len(food_term),
        #                                     end_2=start_2+len(food_term))
        temp_result += food_template.format(food=food_term).strip() + '\n'
    with open(output_file, 'w', encoding="utf-8") as fpw:
        fpw.write("## intent:consult_food\n")
        fpw.write(temp_result)
    with open("food_terms1.txt", 'w', encoding="utf-8") as fpw2:
        for term in terms_ls:
            fpw2.write(term + '\n')


def create_food_data2(terms_ls, output_file, data_count):
    # terms_ls = []
    # terms_ls.extend(clean_food_data1(term_file))
    len_ls1 = len(food_template_ls1)
    len_ls2 = len(food_template_ls2)
    count1 = int(data_count * len_ls1/(len_ls1+len_ls2))
    count2 = int(data_count * len_ls2/(len_ls1+len_ls2))
    # print(count1, count2)
    temp_result = ''
    food_ls2 = food_template_ls2 * (count2 // len_ls2)
    temp_result += '\n'.join(food_ls2) + '\n'
    food_ls1 = food_template_ls1 * (count1 // len_ls1)
    j = 0
    for food_template in food_ls1:
        if j == len(terms_ls):
            j = 0
        temp_result += food_template.format(food=terms_ls[j]) + '\n'
        j += 1
    with open(output_file, 'w', encoding="utf-8") as fpw:
        fpw.write("## intent:consult_food\n")
        fpw.write(temp_result)
    with open("food_terms.txt", 'w', encoding="utf-8") as fpw2:
        for term in terms_ls:
            fpw2.write(term + '\n')


food_terms_ls = clean_food_data1("food_terms2.txt") + list(set(clean_food_data1("food_terms1.txt")))
# create_food_data("food_data", "food_train_data.md")
create_food_data2(food_terms_ls, "food_train_data8.md", 7000)


