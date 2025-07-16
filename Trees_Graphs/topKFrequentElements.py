# Top K Frequent Elements
# 🧩 Problem:
# Given a list of integers and an integer k, return the k most frequent elements.
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

from collections import Counter
import heapq


def topKFrequent(nums, k):
    freq = Counter(nums)
    # sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    # return [item for item, count in sorted_items[:k]]
    return [item for item, _ in heapq.nlargest(k, freq.items(), key=lambda x: x[1])]


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
