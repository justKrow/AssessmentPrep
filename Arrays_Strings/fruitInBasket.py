# 🧩 Next Problem: Fruits into Baskets (aka Longest Substring with At Most 2 Distinct Characters – but framed differently)
# This is exactly the same core logic as the one you just solved, but framed in a more visual / real-world way. Let's reinforce the pattern one more time before switching it up.

# 🔍 Problem Statement:
# You are given an array of characters where each character represents a fruit tree.
# You are allowed to pick only two types of fruits.
# You must pick them from a contiguous subarray (i.e. no skipping).
# Return the length of the longest subarray with at most 2 different types of fruits.
# Input: ['A', 'B', 'C', 'A', 'C']
# Output: 3
# Explanation: ['C', 'A', 'C']

from collections import defaultdict


def mostFruits(fruits, k):
    left = 0
    max_count = 0
    map = defaultdict(int)
    for right in range(len(fruits)):
        map[fruits[right]] += 1
        if len(map) > k:
            map[fruits[left]] -= 1
            if map[fruits[left]] == 0:
                del map[fruits[left]]
            left += 1
        max_count = max(max_count, right - left + 1)
    return max_count


print(mostFruits(['A', 'B', 'C', 'A', 'C'], 2))
