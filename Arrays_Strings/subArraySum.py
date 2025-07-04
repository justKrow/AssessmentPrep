# Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals k.
# nums = [1, 1, 1]
# k = 2
# Output: 2
# (because [1,1] at index 0-1 and index 1-2 both sum to 2)

from collections import defaultdict


def subArraySum(nums, k):
    prefix_sum = 0
    sum_map = defaultdict(int)
    sum_map[0] = 1
    count = 0
    for num in nums:
        prefix_sum += num
        diff = prefix_sum - k
        if diff in sum_map:
            count += sum_map[diff]
        sum_map[prefix_sum] += 1
        print(sum_map)
    return count


print(subArraySum([1, 1, 1], 2))
