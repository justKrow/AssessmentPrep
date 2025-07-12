# 🧩 Next Problem: Longest Repeating Character Replacement
# Problem statement:
# You’re given a string s and an integer k. You can replace at most k characters in the string so that the resulting substring consists of the same character.

# Return the length of the longest substring possible after at most k replacements.

# Example:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the second 'B' with 'A' → "AABAABA", substring "AAAA" length 4.

from collections import defaultdict


def replaceCharacter(s, k):
    left = 0
    max_count = 0
    count = defaultdict(int)
    max_freq = 0
    max_substring = ""
    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(max_freq, count[s[right]])
        window_size = right - left + 1
        if window_size - max_freq > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        if right - left + 1 > max_count:
            max_count = right - left + 1
            max_substring = s[left: right + 1]
    return max_substring


print(replaceCharacter("AABABBA", 1))
