# -*- coding: utf-8 -*-

from traffic_templates import traffic_template1, traffic_template2


def create_traffic_data(term_file, output_file):
    with open(term_file, 'r', encoding="utf-8") as fpr:
        terms_temp_ls = fpr.readlines()
    terms_ls = [term2.strip() for term2 in terms_temp_ls]
    temp_result = ''
    for traffic_term in list(set(terms_ls)):
        temp_result += traffic_template1.format(position=traffic_term).strip() + '\n'

    for i in range(len(terms_ls)):
        if i == len(terms_ls) - 1:
            break
        temp_result += traffic_template2.format(position1=terms_ls[i], position2=terms_ls[i+1]).strip() + '\n'

    with open(output_file, 'w', encoding="utf-8") as fpw:
        fpw.write("## intent:search_traffic\n")
        fpw.write(temp_result)

create_traffic_data("beijing_spots", "traffic_train_data.md")

