# Prompt:
# Given an integer array nums and an integer k, return the kth largest element in the array.

# This problem is a great chance to compare:

# Sorting approach

# Min heap of size k (the efficient way)

import heapq


def sortingApproach(arr, k):
    if k > len(arr) or not arr:
        return []
    arr.sort()
    return arr[-k]


def heapApproach(arr, k):
    if k > len(arr) or not arr:
        return []
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap[0]


print(sortingApproach([1, 2, 3, 5, 6], 2))
print(heapApproach([1, 2, 3, 5, 6], 2))
