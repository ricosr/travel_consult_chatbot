# -*- coding: utf-8 -*-

version = 8

with open("food/food_train_data{}.md".format(version), 'r', encoding="utf-8") as fpr1:
    food_train_ls = fpr1.readlines()

with open("hotel/hotel_train_data{}.md".format(version), 'r', encoding="utf-8") as fpr2:
    hotel_train_ls = fpr2.readlines()

with open("shopping/shopping_train_data{}.md".format(version), 'r', encoding="utf-8") as fpr3:
    shopping_train_ls = fpr3.readlines()

with open("traffic/traffic_train_data{}.md".format(version), 'r', encoding="utf-8") as fpr4:
    traffic_train_ls = fpr4.readlines()

with open("weather/weather_train_data{}.md".format(version), 'r', encoding="utf-8") as fpr5:
    weather_train_ls = fpr5.readlines()

with open("../intent/nlu{}.md".format(version), 'w', encoding="utf-8") as fpw:
    fpw.writelines(food_train_ls)
    fpw.write('\n')
    fpw.writelines(traffic_train_ls)
    fpw.write('\n')
    fpw.writelines(weather_train_ls)
    # fpw.write('\n')
    # fpw.writelines(hotel_train_ls)
    # fpw.write('\n')
    # fpw.writelines(shopping_train_ls)
