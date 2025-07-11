# Minimum Window Substring
# 🔍 Problem:
# You're given two strings s and t.
# Find the smallest window in s that contains all the characters in t (including duplicates).
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

from collections import Counter, defaultdict


def minWindowSubstring(s, t):
    if not s or not t or len(t) > len(s):
        return False
    need = Counter(t)
    left = 0
    min_len = float("inf")
    have = defaultdict(int)
    formed = 0
    required = len(need)
    min_window = ""
    for right in range(len(s)):
        char = s[right]
        have[char] += 1
        if char in need and have[char] == need[char]:
            formed += 1
        while formed == required:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                min_window = s[left:right+1]
            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1
            left += 1
    return min_window


print(minWindowSubstring("ADOBECODEBANC", "ABC"))
