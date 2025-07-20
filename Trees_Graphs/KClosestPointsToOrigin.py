# 🧩 Problem: K Closest Points to Origin
# Prompt:

# You are given an array of points where points[i] = [xᵢ, yᵢ] represents a point on the X-Y plane, and an integer k.

# Return the k closest points to the origin(0, 0).

# The distance between a point (x, y) and the origin is:
# sqrt(x² + y²)
# But we can avoid the square root for comparison purposes (since sqrt is monotonic).

import heapq


def kClosestBruteForce(points, k):
    points.sort(key=lambda x: x[0]**2 + x[1]**2)
    return points[:k]


def kClosestHeap(points, k):
    heap = []
    for x, y in points:
        distance = x ** 2 + y ** 2
        heapq.heappush(heap, (-(distance), [x, y]))
        if len(heap) > k:
            heapq.heappop(heap)
    return [point for distance, point in heap]


print(kClosestBruteForce([[1, 3], [-2, 2], [5, 8], [0, 1]], 2))
print(kClosestHeap([[1, 3], [-2, 2], [5, 8], [0, 1]], 2))
