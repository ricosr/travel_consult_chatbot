# -*- coding:utf-8 -*-

with open("beijing_street.txt", 'r', encoding="gbk") as fpr:
    street_temp_ls = fpr.read().split(',')

street_ls = [street.strip() for street in street_temp_ls if street.strip()]

with open("Scenic_spot", 'r', encoding="utf-8") as fpr:
    spot_temp_ls = fpr.read().replace('\t', ' ').replace('\n', ' ').split(' ')

spot_ls = []
for spot in spot_temp_ls:
    if '.' not in spot and spot:
        spot_ls.append(spot.strip("…"))

final_results = list(set(street_ls + spot_ls))
with open("temp_result", 'w', encoding="utf-8") as fpw:
    for result in final_results:
        fpw.write(result + '\n')

