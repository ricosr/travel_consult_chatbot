# -*- coding: utf-8 -*-

from food_templates import *


def create_food_data(term_file, output_file):
    with open(term_file, 'r', encoding="utf-8") as fpr:
        terms_temp_ls = fpr.readlines()
    terms_ls = [term.split(',')[0] for term in terms_temp_ls]
    temp_result = ''
    for food_term in terms_ls:
        # temp_result += food_template.format(food=food_term, end0=start0+len(food_term), end1=start1+len(food_term),
        #                                     end2=start2+len(food_term), end3=start3+len(food_term),
        #                                     end_0=start_0+len(food_term), end_1=start_1+len(food_term),
        #                                     end_2=start_2+len(food_term))
        temp_result += food_template.format(food=food_term).strip() + '\n'
    with open(output_file, 'w', encoding="utf-8") as fpw:
        fpw.write("## intent:search_food\n")
        fpw.write(temp_result)

create_food_data("food_data", "food_train_data.md")
