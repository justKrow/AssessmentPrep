# Find the length of the longest substring with no more than K distinct characters.

# def longestSubString(word, k):
#     map = {}
#     left = 0
#     for right in range(0, len(word) + 1):
#         # map[word[left:right+1]] = len(set(word[left:right+1]))
#         # if len(set(word[left:right+1])) <= k:
#         #     if len(max_subString) < len(word[left:right+1]):
#         #         max_subString = word[left:right+1]
#         #         left = right
#         if len(set(word[left:right+1])) <= k:
#             map[word[left:right+1]] = len(word[left:right+1])
#         else:
#             left += 1
#     return max(map, key=map.get)

from collections import defaultdict


def longestSubString(word, k):
    char_count = defaultdict(int)
    left = 0
    max_len = 0

    for right in range(len(word)):
        char_count[word[right]] += 1

        # Shrink the window if more than k distinct characters
        while len(char_count) > k:
            char_count[word[left]] -= 1
            if char_count[word[left]] == 0:
                del char_count[word[left]]
            left += 1

        max_len = max(max_len, right - left + 1)
    return max_len


print(longestSubString("eceba", 2))  # Output: 3
