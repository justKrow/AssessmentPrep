# Longest Repeating Character Replacement
# You are given a string s and an integer k. You can replace at most k characters in the string so that the entire resulting substring consists of the same character.

# Return the length of the longest possible substring you can get.
# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the second 'B' with 'A' to get "AABA**A**BA" → "AAAA"

from collections import defaultdict


def longestestRepeatingCharacterReplacement(word, k):
    max_len = 0
    left = 0
    count = defaultdict(int)
    max_freq = 0
    for right in range(len(word)):
        count[word[right]] += 1
        # max_freq = max(count.values())
        max_freq = max(max_freq, count[word[right]])
        if len(word[left:right+1]) - max_freq > k:
            count[word[left]] -= 1
            if count[word[left]] == 0:
                del count[word[left]]
            left += 1
        max_len = max(max_len, len(word[left:right+1]))
    return max_len


print(longestestRepeatingCharacterReplacement("AABABBA", 1))
