# 🧩 Problem Statement:
# Given a string s, find the length of the longest substring without repeating characters.
# Input:  s = "abcabcbb"
# Output: 3  # The answer is "abc"

def longestSubString(string):
    left = 0
    seen = set()
    max_count = 0
    for right in range(len(string)):
        while string[right] in seen:
            seen.remove(string[left])
            left += 1
        seen.add(string[right])
        max_count = max(max_count, len(seen))
    return max_count


print(longestSubString("abcabcbb"))
