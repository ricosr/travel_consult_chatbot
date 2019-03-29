# -*- coding: utf-8 -*-

from consult.dinning import dinning_handle
from slots.consult_slot import dinning_slot

database_address = "mongodb://xxx:xxx@209.97.xxx.xxx:27017/xxx"
database_name = "xxx"

intent_config = {
    '1b': dinning_handle
}

slot_config = {
    '1b': dinning_slot
}

