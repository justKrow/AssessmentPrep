# 🧩 Problem: Longest Substring with At Most Two Distinct Characters
# Prompt:
# Given a string s, return the length of the longest substring that contains at most two distinct characters.
# Input: "eceba"
# Output: 3
# Explanation: "ece" is the longest substring with at most 2 distinct characters.

from collections import defaultdict


def longestSubString(s, k):
    left = 0
    map = defaultdict(int)
    max_count = 0
    for right in range(len(s)):
        map[s[right]] += 1
        if len(map) > k:
            map[s[left]] -= 1
            if map[s[left]] == 0:
                del map[s[left]]
            left += 1
        max_count = max(right - left + 1, max_count)
    return max_count


print(longestSubString("eceba", 2))
