# Problem: Given a list of numbers, return a list where each element is the sum of all the elements up to that index (inclusive).

# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]

def runningSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums


print(runningSum([]))
