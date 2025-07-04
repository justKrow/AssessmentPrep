# Problem: Two Sum
# Prompt:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to the target.

# You may assume that each input has exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1](because nums[0] + nums[1] == 9)

def twoSum(nums, target):
    seen = {}
    index = 0
    for num in nums:
        complement = target - num
        if complement in seen:
            return [seen[complement], index]
        seen[num] = index
        index += 1


print(twoSum([2, 7, 11, 15], 9))
