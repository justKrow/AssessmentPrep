# Problem: Majority Element
# Prompt:
# Given an array nums, return the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
# ✅ Examples:
# nums = [3, 2, 3]
# Output:3
#
# Input:
# nums = [2, 2, 1, 1, 1, 2, 2]
# Output:2

from collections import Counter


def majority(nums):
    # count = Counter(nums)
    # majority_count = len(nums) // 2
    # for key, value in count.items():
    #     if value > majority_count:
    #         return key
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        if candidate == num:
            count += 1
        else:
            count -= 1

        # Step 2: Verify the candidate
    # if nums.count(candidate) > len(nums) // 2:
    #     return candidate
    # else:
    #     return None  # No majority element
    return candidate


print(majority([2, 2, 1, 1, 1, 2, 2]))
