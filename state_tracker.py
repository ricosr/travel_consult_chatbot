# -*- coding: utf-8 -*-


class State:
    def __init__(self, slot_key):
        self.last_slot_key = slot_key
        self.state_dict = {}

    def update_last_slot_key(self, slot_key):
        self.last_slot_key = slot_key

    def get_last_slot_key(self):
        return self.last_slot_key

    def add_one_state(self, slot_key, slot_value, confidence):
        self.state_dict[slot_key] = {"slot_value": slot_value, "confidence": confidence}

    def update_slot_value(self, slot_key, slot_value):
        self.state_dict[slot_key]["slot_value"] = slot_value

    def update_confidence(self, slot_key, confidence):
        self.state_dict[slot_key]["confidence"] = confidence

    def get_state(self):
        return self.state_dict

    def get_slot_value(self, slot_key):
        return self.state_dict[slot_key]["slot_value"]

    def get_confidence(self, slot_key):
        return self.state_dict[slot_key]["confidence"]

    def update_all_state(self, ie_values_dict):
        for k, v in ie_values_dict.items():
            if v and v != 0:  # TODO: state tracker
                if k in self.get_state():
                    if self.get_slot_value(k) == v:
                        self.update_confidence(k, 1)
                    else:
                        self.update_confidence(k, 0.5)
                else:
                    self.add_one_state(k, v, 0.5)

    def get_current_slot(self, current_slot):
        for slot_key, value_dict in self.get_state().items():
            if self.get_confidence(slot_key) == 1:
                current_slot[slot_key] = value_dict["slot_value"]

    def get_need_to_confirm(self):


    def judge_dialogue_state(self):
        for slot_key, value_dict in self.state_dict.items():
            if value_dict["slot_value"] is not None and value_dict["slot_value"] != 0 and value_dict["confidence"] == 1:
                continue
            else:
                return False
        return True   # all slots are OK


