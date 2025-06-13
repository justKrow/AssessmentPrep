# Next Problem: “Two Sum II – Input Array Is Sorted”
# Difficulty: Easy
# Concepts: Two Pointers, Arrays

# 📜 Prompt:
# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number.

# Return the indices of the two numbers (1-indexed) as an array [index1, index2], where index1 < index2.

# You may assume that each input has exactly one solution, and you may not use the same element twice.

# 💡 Example:
# python
# Copy
# Edit
# Input: numbers = [2, 7, 11, 15], target = 9  
# Output: [1, 2]  # Because 2 + 7 = 9

# Input: numbers = [1, 2, 3, 4, 4, 9, 56, 90], target = 8  
# Output: [4, 5]  # 4 + 4 = 8

numbers = [1, 2, 3, 4, 4, 9, 56, 90]
target = 8  

def twoSumTwoPointer(numbers, target):
    left = 0 
    right = len(numbers) - 1
    while right > left:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left+1, right+1]
        elif sum > target:
            right -= 1 
        else:
            left += 1
    return []

print(twoSumTwoPointer(numbers, target))