# Top K Frequent Elements
# 🧩 Problem Statement:
# Given an integer array nums, return the k most frequent elements.
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]  # 1 appears 3 times, 2 appears 2 times

from collections import Counter
import heapq


def findTopKFrequentElements(nums, k):
    counter = Counter(nums)
    # return [item for item, freq in sorted(counter.items(), key=lambda x: x[1], reverse=True)[:k]]
    heap = []
    for num, freq in counter.items():
        heapq.heappush(heap, (freq, num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for freq, num in heap]


print(findTopKFrequentElements([1, 1, 1, 2, 2, 3], 2))
