# -*- coding: utf-8 -*-


def read_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as fpr:
        terms_ls = fpr.readlines()
    return terms_ls


def write_file(out_path, data_ls):
    with open(out_path, 'w', encoding="utf-8") as fpw:
        fpw.writelines(data_ls)


def generate_dict(origin_dict_path, supplement_terms):
    with open(origin_dict_path, 'r', encoding="utf-8") as fpr:
        terms_ls = fpr.readlines()
    tmp_terms_ls = [term.split(' ')[0].strip() for term in terms_ls]
    new_terms = []
    for sup_term in supplement_terms:
        if sup_term.strip() not in tmp_terms_ls:
            new_terms.append(sup_term.strip() + ' 3' + ' n' + '\n')
    terms_ls.extend(new_terms)
    write_file("new_dict.txt", terms_ls)


food_terms = read_file("food/food_terms.txt")
hotel_terms = read_file("hotel/hotel_terms.txt")
shopping_terms = read_file("shopping/shopping_terms.txt")
traffic_terms = read_file("traffic/traffic_terms.txt")
generate_dict("dict.txt", food_terms+hotel_terms+shopping_terms+traffic_terms)

