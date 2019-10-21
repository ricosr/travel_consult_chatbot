# -*- coding: utf-8 -*-

from hotel_templates import *


def clean_food_data1(term_file):
    with open(term_file, 'r', encoding="utf-8") as fpr:
        terms_temp_ls = fpr.readlines()
    terms_ls = [term2.strip() for term2 in terms_temp_ls]
    return terms_ls


def create_hotel_data(term_file, output_file):
    terms_ls = []
    terms_ls.extend(clean_food_data1(term_file))
    temp_result = ''
    for hotel_term in list(set(terms_ls)):
        temp_result += hotel_template.format(hotel=hotel_term).strip() + '\n'
    with open(output_file, 'w', encoding="utf-8") as fpw:
        fpw.write("## intent:consult_hotel\n")
        fpw.write(temp_result)
    with open("hotel_terms.txt", 'w', encoding="utf-8") as fpw2:
        for term in terms_ls:
            fpw2.write(term + '\n')


def create_hotel_data2(term_file, output_file, data_count):
    terms_ls = []
    terms_ls.extend(clean_food_data1(term_file))
    len_ls1 = len(hotel_template_ls1)
    len_ls2 = len(hotel_template_ls2)
    count1 = int(data_count * len_ls1/(len_ls1+len_ls2))
    count2 = int(data_count * len_ls2/(len_ls1+len_ls2))
    temp_result = ''
    hotel_ls2 = hotel_template_ls2 * (count2 // len_ls2)
    temp_result += '\n'.join(hotel_ls2) + '\n'
    hotel_ls1 = hotel_template_ls1 * (count1 // len_ls1)
    j = 0
    for hotel_template in hotel_ls1:
        if j == len(terms_ls):
            j = 0
        temp_result += hotel_template.format(hotel=terms_ls[j]) + '\n'
        j += 1
    with open(output_file, 'w', encoding="utf-8") as fpw:
        fpw.write("## intent:consult_hotel\n")
        fpw.write(temp_result)
    with open("hotel_terms.txt", 'w', encoding="utf-8") as fpw2:
        for term in terms_ls:
            fpw2.write(term + '\n')

# create_hotel_data("hotel_ls", "hotel_train_data.md")

create_hotel_data2("hotel_ls", "hotel_train_data7.md", 3000)
