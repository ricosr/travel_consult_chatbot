# -*- coding: utf-8 -*-

from flow_structure.consult.consult_food_flow import consult_food_handle
from flow_structure.consult.consult_traffic_flow import consult_traffic_handle
from flow_structure.consult.consult_weather_flow import consult_weather_handle
from flow_structure.plan.plan_ticket_flow import plan_ticket_handle
from flow_structure.plan.plan_scenic_spot_flow import plan_scenic_spot_handle
from slots.consult_slot import consult_food_slot, consult_traffic_slot, consult_weather_slot
from slots.plan_slot import plan_ticket_slot, plan_scenic_spot_slot

time_out = 60

database_address = "mongodb://xxx:xxxx@xxx.xxx.xxx.xxx:27017/admin"
database_name = "Travel_DB"

intent_model_name = "models8"
confirm_model_name = "confirm_model6"

handle_config = {
    'consult_food': consult_food_handle,
    'consult_traffic': consult_traffic_handle,
    'consult_weather': consult_weather_handle,
    'plan_ticket': plan_ticket_handle,
    'plan_scenic_spot': plan_scenic_spot_handle
}

slot_config = {
    'consult_food': consult_food_slot,
    'consult_traffic': consult_traffic_slot,
    'consult_weather': consult_weather_slot,
    'plan_ticket': plan_ticket_slot,
    'plan_scenic_spot': plan_scenic_spot_slot
}

# slot_state_config = {
#     '1b': dinning_slot_state
# }

db_collection_config = {   # TODO: database is not done
    'consult_food': "restaurant",
    'consult_traffic': "",
    'consult_weather': "",
    'plan_ticket': "",
    "plan_scenic_spot": ""
}

plan_intent_ls = ["plan_scenic_spot"]    # TODO: "plan_ticket", "plan_hotel"
