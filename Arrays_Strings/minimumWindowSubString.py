# Given two strings s and t, return the minimum window in s that contains all the characters in t.
# If no such window exists, return an empty string.
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

from collections import Counter, defaultdict


def minWindow(s, t):
    if not s or not t:
        return ""
    window_count = defaultdict(int)
    t_count = Counter(t)
    required = len(t_count)
    result = [-1, -1]
    result_len = float("inf")
    have = 0
    left = 0
    min_window = {}
    for right in range(len(s)):
        char = s[right]
        window_count[char] += 1
        if char in t_count and window_count[char] == t_count[char]:
            have += 1
        while have == required:
            if right - left + 1 < result_len:
                result = [left, right]
                result_len = right - left + 1
            window_count[s[left]] -= 1
            if s[left] in t_count and window_count[s[left]] < t_count[s[left]]:
                have -= 1
            left += 1
        l, r = result
    return s[l:r+1] if result_len != float("inf") else ""


print(minWindow("ADOBECODEBANC", "ABC"))
