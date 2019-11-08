# -*- coding: utf-8 -*-

from traffic_templates import *


def clean_traffic_data1(term_file):
    with open(term_file, 'r', encoding="utf-8") as fpr:
        terms_temp_ls = fpr.readlines()
    terms_ls = [term2.strip() for term2 in terms_temp_ls]
    return terms_ls


def create_traffic_data(term_file, output_file):
    terms_ls = []
    terms_ls.extend(clean_traffic_data1(term_file))
    temp_result = ''
    for traffic_term in list(set(terms_ls)):
        temp_result += traffic_template1.format(destination=traffic_term).strip() + '\n'

    for i in range(len(terms_ls)):
        if i == len(terms_ls) - 1:
            break
        temp_result += traffic_template2.format(departure=terms_ls[i], destination=terms_ls[i+1]).strip() + '\n'

    with open(output_file, 'w', encoding="utf-8") as fpw:
        fpw.write("## intent:consult_traffic\n")
        fpw.write(temp_result)
    with open("traffic_terms.txt", 'w', encoding="utf-8") as fpw2:
        for term in terms_ls:
            fpw2.write(term + '\n')


def create_traffic_data2(term_file, vehicle_terms, output_file, data_count):
    vehicle_terms = clean_traffic_data1(vehicle_terms)
    terms_ls = []
    terms_ls.extend(clean_traffic_data1(term_file))
    len_ls1 = len(traffic_template_ls_1a) + len(traffic_template_ls_1b) + len(traffic_template_ls_1c)
    len_ls2 = len(traffic_template_ls2)
    count1a = int(data_count * len(traffic_template_ls_1a)/(len_ls1+len_ls2))
    count1b = int(data_count * len(traffic_template_ls_1b)/(len_ls1+len_ls2))
    count1c = int(data_count * len(traffic_template_ls_1c)/(len_ls1+len_ls2))
    count2 = int(data_count * len_ls2/(len_ls1+len_ls2))
    # print(count1a, count1b, count2)
    temp_result = ''
    traffic_ls2 = traffic_template_ls2 * (count2 // len_ls2)
    temp_result += '\n'.join(traffic_ls2) + '\n'
    traffic_ls_1a = traffic_template_ls_1a * (count1a // len(traffic_template_ls_1a))
    traffic_ls_1b = traffic_template_ls_1b * (count1b // len(traffic_template_ls_1b))
    traffic_ls_1c = traffic_template_ls_1c * (count1c // len(traffic_template_ls_1c))
    i = 0
    j = 0
    for traffic_template in traffic_ls_1a:
        if j == len(terms_ls):
            j = 0
        if i == len(vehicle_terms):
            i = 0
        temp_result += traffic_template.format(destination=terms_ls[j], vehicle=vehicle_terms[i]) + '\n'
        i += 1
        j += 1
    i = 0
    j = 0
    for traffic_template in traffic_ls_1b:
        if j >= len(terms_ls):
            j = 0
        if i == len(vehicle_terms):
            i = 0
        temp_result += traffic_template.format(departure=terms_ls[j], destination=terms_ls[j+1], vehicle=vehicle_terms[i]) + '\n'
        i += 1
        j += 2
    j = 0
    for traffic_template in traffic_ls_1c:
        if j >= len(terms_ls):
            j = 0
        temp_result += traffic_template.format(departure=terms_ls[j], destination=terms_ls[j + 1]) + '\n'
        j += 2
    with open(output_file, 'w', encoding="utf-8") as fpw:
        fpw.write("## intent:consult_traffic\n")
        fpw.write(temp_result)
    with open("traffic_terms.txt", 'w', encoding="utf-8") as fpw2:
        for term in terms_ls+vehicle_terms:
            fpw2.write(term + '\n')

# create_traffic_data("beijing_spots", "traffic_train_data.md")
create_traffic_data2("beijing_spots", "vehicle", "traffic_train_data8.md", 8000)
