# 🧩 Next Problem: Sliding Window Maximum
# Problem Statement:

# You are given an array of integers nums, and an integer k.

# You need to return a list of the maximum value in every sliding window of size k.
# Input: nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
# Output: [3, 3, 5, 5, 6, 7]
# Explanation:

# Window [1,3,-1] → max is 3

# Window [3,-1,-3] → max is 3

# Window [-1,-3,5] → max is 5

# Window [-3,5,3] → max is 5

# Window [5,3,6] → max is 6

# Window [3,6,7] → max is 7
from collections import deque


def slidingWindowMax(nums, k):
    # left = 0
    dq = deque()
    max_arr = []
    # for right in range(k-1, len(nums)):
    #     max_arr.append(max(nums[left:right+1]))
    #     left += 1
    for i in range(len(nums)):
        if dq and dq[0] < i - k + 1:
            dq.popleft()

        while dq and dq[-1] < nums[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            max_arr.append(nums[dq[0]])

    return (max_arr)


print(slidingWindowMax([1, 3, -1, -3, 5, 3, 6, 7], 3))
