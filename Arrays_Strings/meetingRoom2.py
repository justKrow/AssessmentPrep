# ✅ Problem: Meeting Rooms II
# 🔍 Prompt:
# Given an array of meeting time intervals intervals where intervals[i] = [start_i, end_i],
# return the minimum number of conference rooms required.
# Input: [[0,30],[5,10],[15,20]]
# Output: 2

import heapq


def minimumRooms(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    heap = []
    for interval in intervals:
        start, end = interval
        if heap and start >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, end)
    return len(heap)


print(minimumRooms([[0, 30], [5, 10], [15, 20]]))
