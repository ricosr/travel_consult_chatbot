# -*- coding: utf-8 -*-

from hotel_templates import hotel_template


def create_hotel_data(term_file, output_file):
    with open(term_file, 'r', encoding="utf-8") as fpr:
        terms_temp_ls = fpr.readlines()
    terms_ls = [term2.strip() for term2 in terms_temp_ls]
    temp_result = ''
    for hotel_term in list(set(terms_ls)):
        temp_result += hotel_template.format(hotel=hotel_term).strip() + '\n'
    with open(output_file, 'w', encoding="utf-8") as fpw:
        fpw.write("## intent:search_hotel\n")
        fpw.write(temp_result)

create_hotel_data("hotel_ls", "hotel_train_data.md")
