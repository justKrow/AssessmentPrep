# You are given an integer array nums. Implement a class that supports:

# sumRange(i, j) → returns the sum of elements between indices i and j(inclusive).
# nums = [-2, 0, 3, -5, 2, -1]
# sumRange(0, 2) → 1   # -2 + 0 + 3
# sumRange(2, 5) → -1  # 3 + (-5) + 2 + (-1)
# sumRange(0, 5) → -3

class NumArray:
    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, i, j):
        return self.prefix[j+1] - self.prefix[i]
