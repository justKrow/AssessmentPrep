# You're going to implement a data structure that supports the following operations in O(1) time:

# ✅ Operations:
# insert(val) – Inserts an item val to the set if not already present. Returns True if inserted, False otherwise.

# remove(val) – Removes an item val from the set if present. Returns True if removed, False otherwise.

# getRandom() – Returns a random element from the current set of elements. Each element must have the same probability of being returned.

import random


class idrDataStructure:
    def __init__(self):
        self.values = []
        self.value_to_index = {}

    def insert(self, value):
        if value not in self.value_to_index:
            self.values.append(value)
            self.value_to_index[value] = len(self.values) - 1
            return True
        return False

    def remove(self, value):
        if value in self.value_to_index:
            index = self.value_to_index[value]
            last_value = self.values[-1]
            self.values[index] = last_value
            self.value_to_index[last_value] = index
            self.values.pop()
            del self.value_to_index[value]
            return True
        return False

    def getRandom(self):
        return random.choice(self.values)


obj = idrDataStructure()
obj.insert(1)         # True
obj.remove(2)         # False
obj.insert(2)         # True
obj.getRandom()       # 1 or 2
obj.remove(1)         # True
obj.insert(2)         # False (already present)
obj.getRandom()
