# -*- coding: utf-8 -*-


class State:
    def __init__(self):
        # self.state_no = -1
        # self.slot_key = -1
        # self.slot_value = -1
        # self.confidence = -1
        self.state_dict = {}

    def add_one_state(self, state_no, slot_key, slot_value, confidence):
        self.state_dict[state_no] = {"slot_key": slot_key, "slot_value": slot_value, "confidence": confidence}

    def update_slot_value(self, state_no, slot_value):
        self.state_dict[state_no]["slot_value"] = slot_value

    def update_confidence(self, state_no, confidence):
        self.state_dict[state_no]["confidence"] = confidence

    def get_state(self, slot_no):
        return self.state_dict

    def get_slot_value(self, state_no):
        return self.state_dict[state_no]["slot_value"]

    def get_confidence(self, state_no):
        return self.state_dict[state_no]["confidence"]


