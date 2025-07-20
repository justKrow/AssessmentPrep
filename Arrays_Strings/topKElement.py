# ✅ Problem: Top K Frequent Elements
# 🔍 Problem Statement:
# Given an integer array nums and an integer k, return the k most frequent elements.
# The answer can be in any order.
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

from collections import Counter


def topKFrequent(nums, k):
    freq_map = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    print(buckets)

    for num, freq in freq_map.items():
        buckets[freq].append(num)

    print(buckets)
    res = []
    for i in range(len(buckets)-1, 0, -1):
        for num in buckets[i]:
            res.append(num)
            if len(res) == k:
                return res


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
