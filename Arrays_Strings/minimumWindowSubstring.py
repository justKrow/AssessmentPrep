# Next Problem(Day 4 Topic): Minimum Window Substring
# This problem mixes hash maps + sliding window — one of the most asked string problems in interviews.

# 🔍 Prompt:
# Given two strings s and t, return the minimum window substring of s such that every character in t(including duplicates) is included in the window.

# If no such window exists, return "".
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

from collections import Counter, defaultdict


def minimumWindow(s, t):
    if not s or not t or len(t) > len(s):
        return ""
    left = 0
    t_counter = Counter(t)
    required = len(t_counter)
    formed = 0
    seen = defaultdict(int)
    min_len = float("inf")
    sub_string = [-1, -1]
    for right in range(len(s)):
        seen[s[right]] += 1
        if s[right] in t_counter and seen[s[right]] == t_counter[s[right]]:
            formed += 1
        while formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                sub_string = [left, right]
            seen[s[left]] -= 1
            if s[left] in t_counter and seen[s[left]] < t_counter[s[left]]:
                formed -= 1
            left += 1
    return s[sub_string[0]: sub_string[1] + 1]


print(minimumWindow("ADOBECODEBANC", "ABC"))
