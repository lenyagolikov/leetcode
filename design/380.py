# https://leetcode.com/problems/insert-delete-getrandom-o1/

import random


class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.keys = {}

    def insert(self, val: int) -> bool:
        if val in self.keys:
            return False

        self.keys[val] = len(self.nums)
        self.nums.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.keys:
            return False

        val_index = self.keys[val]
        last = self.nums[-1]

        self.nums[val_index], self.nums[-1] = self.nums[-1], self.nums[val_index]
        self.keys[last] = self.keys[val]

        self.nums.pop()
        del self.keys[val]

        return True

    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]
