# -*- coding: utf-8 -*-

from shopping_templates import *


def clean_shopping_data1(term_file, term_file2):
    with open(term_file, 'r', encoding="utf-8") as fpr:
        terms_temp_ls = fpr.readlines()
    with open(term_file2, 'r', encoding="utf-8") as fpr2:
        terms_temp_ls2 = list(set(fpr2.readlines()))
    terms_ls2 = [term2.strip() for term2 in terms_temp_ls2]
    terms_ls = []
    for term in terms_temp_ls:
        tmp_term = term.split(',')[1].strip()
        if '/' in tmp_term:
            terms_ls.extend(tmp_term.split('/'))
        else:
            terms_ls.append(tmp_term)
    terms_ls.extend(terms_ls2)
    return terms_ls


def create_shopping_data(term_file, term_file2, output_file):
    terms_ls = []
    terms_ls.extend(clean_shopping_data1(term_file, term_file2))
    temp_result = ''
    for commodity_term in list(set(terms_ls)):
        temp_result += commodity_template.format(commodity=commodity_term).strip() + '\n'
    with open(output_file, 'w', encoding="utf-8") as fpw:
        fpw.write("## intent:consult_commodity\n")
        fpw.write(temp_result)
    with open("shopping_terms.txt", 'w', encoding="utf-8") as fpw2:
        for term in terms_ls:
            fpw2.write(term + '\n')


def create_shopping_data2(term_file, term_file2, output_file, data_count):
    terms_ls = []
    terms_ls.extend(clean_shopping_data1(term_file, term_file2))

    len_ls1 = len(commodity_template_ls1)
    len_ls2 = len(commodity_template_ls2)
    count1 = int(data_count * len_ls1/(len_ls1+len_ls2))
    count2 = int(data_count * len_ls2/(len_ls1+len_ls2))
    # print(count1, count2)
    temp_result = ''
    commodity_ls2 = commodity_template_ls2 * (count2 // len_ls2)
    temp_result += '\n'.join(commodity_ls2) + '\n'
    commodity_ls1 = commodity_template_ls1 * (count1 // len_ls1)
    j = 0
    for commodity_template in commodity_ls1:
        if j == len(terms_ls):
            j = 0
        temp_result += commodity_template.format(commodity=terms_ls[j]) + '\n'
        j += 1
    with open(output_file, 'w', encoding="utf-8") as fpw:
        fpw.write("## intent:consult_commodity\n")
        fpw.write(temp_result)
    with open("shopping_terms.txt", 'w', encoding="utf-8") as fpw2:
        for term in terms_ls:
            fpw2.write(term + '\n')


# create_shopping_data("categories.csv", "brands", "shopping_train_data.md")
create_shopping_data2("categories.csv", "brands", "shopping_train_data7.md", 3000)

