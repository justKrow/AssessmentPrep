# Problem: Longest Repeating Character Replacement

# Prompt:
# You are given a string s and an integer k. You can choose any character in the string and replace it with any other uppercase English letter, at most k times.

# Return the length of the longest substring containing the same letter you can get after performing the operation at most k times.

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'B' in "AABA**B**BA" with 'A' → "AAAA", length 4.

from collections import defaultdict


def characterReplacement(s, k):
    count = defaultdict(int)
    left = 0
    max_length = 0

    for right in range(len(s)):
        count[s[right]] += 1
        max_freq = max(count.values())
        window_size = right - left + 1
        if window_size - max_freq > k:
            count[s[left]] -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length


print(characterReplacement("AABABBA", 1))
