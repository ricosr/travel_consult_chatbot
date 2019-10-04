# -*- coding: utf-8 -*-

import time

# not mandatory: 0

dinning_slot = {
    "restaurant": None,  # 0
    "food": 0,           # 1
    "area": 0,           # 2
    "price": 0           # 3
}
# dinning_slot_state = ["restaurant", "food", "area", "price", "done", "change"]

food_slot = {
    "food": None,
    "restaurant": None,
    "location": 0
}

traffic_slot = {
    "departure": None,
    "destination": None,
    "vehicle": None,
    "departure_time": time.strftime("%Y%m%d_%H%M%S",time.localtime(time.time()))
}

