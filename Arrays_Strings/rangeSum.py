# 🧩 Problem: Range Sum Query – Immutable
# You're given an integer array nums. Implement a class with a method that:

# Initializes with the array.

# Has a method sumRange(i, j) that returns the sum of the numbers between indices i and j inclusive.

# 📌 Constraints:

# You will be calling sumRange(i, j) multiple times.

# So aim for O(1) time per query, even if it costs O(n) preprocessing.

class rangeSum:
    def __init__(self, num_array):
        self.num_array = num_array
        self.prefix = [0]
        for num in self.num_array:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right+1] - self.prefix[left]


print(rangeSum([1, 2, 3, 4, 5, 6]).prefix)
print(rangeSum([1, 2, 3, 4, 5, 6]).sumRange(1, 3))
