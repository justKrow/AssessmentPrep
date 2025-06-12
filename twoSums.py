# Given an array of integers nums and a target, return indices of the two numbers such that they add up to the target.

nums = [1, 3, 4, 5, 62, 5]
result = []
target = 7


def twoSum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


print(twoSum(nums, target))
