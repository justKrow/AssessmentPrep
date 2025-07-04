# Problem: Sliding Window Maximum
# Prompt:

# You are given an array of integers nums, and an integer k.
# There is a sliding window of size k which moves from the left to the right side of the array.
# You need to return the maximum in each window.
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]

# def slidingMaximum(arr, k):
#     left = 0
#     max_list = []
#     for right in range(k-1, len(arr)):
#         max_list.append(max(arr[left:right+1]))
#         left += 1
#     return max_list


# print(slidingMaximum([1, 3, -1, -3, 5, 3, 6, 7], 3))

from collections import deque


def slidingMaximum(nums, k):
    q = deque()
    result = []

    for i in range(len(nums)):
        # Remove elements outside the window
        while q and q[0] < i - k + 1:
            q.popleft()

        # Remove all elements smaller than current
        while q and nums[q[-1]] < nums[i]:
            q.pop()

        # Add current index
        q.append(i)

        # Start adding results when window is full
        if i >= k - 1:
            result.append(nums[q[0]])  # Front is max

    return result
