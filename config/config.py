# -*- coding: utf-8 -*-

from flow_structure.consult.dinning import dinning_handle
from flow_structure.consult.consult_food_flow import consult_food_handle
from flow_structure.consult.consult_traffic_flow import consult_traffic_handle
from slots.consult_slot import dinning_slot, consult_food_slot, consult_traffic_slot
from slots.plan_slot import plan_ticket_slot

database_address = "mongodb://xxx:xxxx@xxx.xxx.xxx.xxx:27017/admin"
database_name = "Travel_DB"

intent_model_name = "models5"
confirm_model_name = "confirm_model"

handle_config = {
    'search_food': consult_food_handle,
    'search_traffic': consult_traffic_handle,
    'plan_ticket': plan_ticket_handle
}

slot_config = {
    'search_food': consult_food_slot,
    'search_traffic': consult_traffic_slot,
    'plan_ticket': plan_ticket_slot
}

# slot_state_config = {
#     '1b': dinning_slot_state
# }

db_collection_config = {   # TODO: database is not done
    'search_food': "restaurant",
    'search_traffic': "",
    'plan_ticket': ""
}

plan_intent_ls = ["plan_ticket"]    # TODO: "plan_scenic", "plan_hotel"
