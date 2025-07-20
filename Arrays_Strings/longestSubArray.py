# Problem: Longest Subarray with Sum ≤ K
# 🔍 Prompt:
# Given an array of integers nums and an integer k, return the length of the longest subarray whose sum is less than or equal to k.

def longestSubarray(nums, k):
    left = 0
    max_len = 0
    sum = 0
    for right in range(len(nums)):
        sum += nums[right]
        while sum > k:
            sum = sum - nums[left]
            left += 1
        max_len = max(max_len, right-left+1)
    return max_len


print(longestSubarray([2, -1, 2], 4))
