# Permutation in String
# 🧩 Problem:
# Given two strings s1 and s2, return True if s2 contains a permutation of s1, or False otherwise.

# In other words, return True if one of s1's permutations is a substring of s2.
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: False

from collections import Counter, defaultdict


def hasPermutation(s1, s2):
    if not s1 or not s2 or len(s1) > len(s2):
        return False
    s1_count = Counter(s1)
    window_count = defaultdict(int)
    left = 0

    for right in range(len(s2)):
        window_count[s2[right]] += 1

        # Shrink window if bigger than s1 length
        if right - left + 1 > len(s1):
            window_count[s2[left]] -= 1
            if window_count[s2[left]] == 0:
                del window_count[s2[left]]
            left += 1

        # Check after sliding window updated
        if right - left + 1 == len(s1) and window_count == s1_count:
            return True

    return False


print(hasPermutation("ab", "eidbaooo"))  # Should print True
