# -*- coding: utf-8 -*-

from shopping_templates import commodity_template


def create_shopping_data(term_file, term_file2, output_file):
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
    temp_result = ''
    for commodity_term in list(set(terms_ls)):
        temp_result += commodity_template.format(commodity=commodity_term).strip() + '\n'
    with open(output_file, 'w', encoding="utf-8") as fpw:
        fpw.write("## intent:search_commodity\n")
        fpw.write(temp_result)

create_shopping_data("categories.csv", "brands", "shopping_train_data.md")