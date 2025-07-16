# 🧩 Problem: Kth Largest Element in an Array
# 🔍 Problem Statement:
# Given an integer array nums and an integer k, return the kth largest element in the array.

# Note: It’s not the kth distinct element — duplicates count.
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5  # The 2nd largest element is 5

import heapq


def findKthLargest(nums, k):
    heap = []
    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


print(findKthLargest([3, 2, 1, 5, 6, 4], 2))
