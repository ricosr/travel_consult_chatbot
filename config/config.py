# -*- coding: utf-8 -*-

from consult.dinning import dinning_handle
from slots.consult_slot import dinning_slot

database_address = ""
database_name = ""

intent_config = {
    '1b': dinning_handle
}

slot_config = {
    '1b': dinning_slot
}

# slot_state_config = {
#     '1b': dinning_slot_state
# }

db_collection_config = {
    '1b': "restaurant"
}
