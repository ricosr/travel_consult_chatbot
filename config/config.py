# -*- coding: utf-8 -*-

from consult.dinning import dinning_handle
from consult.food_handle import search_food_handle
from slots.consult_slot import dinning_slot, food_slot

database_address = "mongodb://super_sr:comppolyuhk@209.97.166.185:27017/admin"
database_name = "Travel_DB"

intent_model_name = "models1"

handle_config = {
    'search_food': search_food_handle
}

slot_config = {
    'search_food': food_slot
}

# slot_state_config = {
#     '1b': dinning_slot_state
# }

db_collection_config = {
    'search_food': "restaurant"
}
