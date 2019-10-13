# -*- coding: utf-8 -*-

from flow_structure.consult.dinning import dinning_handle
from flow_structure.consult.consult_food_flow import consult_food_handle
from slots.consult_slot import dinning_slot, consult_food_slot

database_address = "mongodb://super_sr:comppolyuhk@209.97.166.185:27017/admin"
database_name = "Travel_DB"

intent_model_name = "models3"
confirm_model_name = "confirm_model"

handle_config = {
    'search_food': consult_food_handle
}

slot_config = {
    'search_food': consult_food_slot
}

# slot_state_config = {
#     '1b': dinning_slot_state
# }

db_collection_config = {
    'search_food': "restaurant"
}
