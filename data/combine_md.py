# -*- coding: utf-8 -*-


with open("food/food_train_data3.md", 'r', encoding="utf-8") as fpr1:
    food_train_ls = fpr1.readlines()

with open("hotel/hotel_train_data3.md", 'r', encoding="utf-8") as fpr2:
    hotel_train_ls = fpr2.readlines()

with open("shopping/shopping_train_data3.md", 'r', encoding="utf-8") as fpr3:
    shopping_train_ls = fpr3.readlines()

with open("traffic/traffic_train_data3.md", 'r', encoding="utf-8") as fpr4:
    traffic_train_ls = fpr4.readlines()

with open("nlu3.md", 'w', encoding="utf-8") as fpw:
    fpw.writelines(food_train_ls)
    fpw.write('\n')
    fpw.writelines(hotel_train_ls)
    fpw.write('\n')
    fpw.writelines(shopping_train_ls)
    fpw.write('\n')
    fpw.writelines(traffic_train_ls)
