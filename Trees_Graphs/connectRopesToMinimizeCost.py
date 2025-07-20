# Problem: Connect Ropes to Minimize Cost
# 📘 Problem Statement:
# You are given an array of integers ropes representing the lengths of ropes. You need to connect them all into one rope. The cost to connect two ropes is equal to the sum of their lengths.

# Return the minimum total cost to connect all the ropes.
# Input: [4, 3, 2, 6]
# Output: 29

# Explanation:
# - First, connect 2 + 3 = 5 → total cost = 5
# - Then, connect 4 + 5 = 9 → total cost = 5 + 9 = 14
# - Finally, connect 6 + 9 = 15 → total cost = 14 + 15 = 29

import heapq


def connectRopes(ropes):
    if not ropes or len(ropes) == 0:
        return 0

    heapq.heapify(ropes)
    total_cost = 0
    while len(ropes) > 1:
        first = heapq.heappop(ropes)
        second = heapq.heappop(ropes)
        cost = first + second
        total_cost = total_cost + cost
        heapq.heappush(ropes, cost)
    return total_cost


print(connectRopes([4, 3, 2, 6]))
