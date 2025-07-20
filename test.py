from collections import defaultdict


def subarraySum(nums, k):
    prefix_map = defaultdict(int)
    prefix_map[0] = 1  # base case
    curr_sum = 0
    count = 0

    for num in nums:
        curr_sum += num
        # find if we’ve seen a matching prefix
        count += prefix_map[curr_sum - k]
        prefix_map[curr_sum] += 1

    return count


print(subarraySum([1, 1, 1], 2))
