# Next Problem: Find All Anagrams in a String
# Problem:
# Given two strings s and p, return all start indices of p's anagrams in s.
# You can return the answer in any order.

# Example:
# Input: s = "cbaebabacd", p = "abc"
# Output: [0, 6]
# Explanation:

# Substring starting at index 0 is "cba", which is an anagram of "abc".

# Substring starting at index 6 is "bac", which is an anagram of "abc".

from collections import Counter, defaultdict


def findAllAnagram(s, p):
    if not p or len(p) > len(s):
        return []
    left = 0
    result = []
    p_counter = Counter(p)
    window_counter = defaultdict(int)
    print(dict(p_counter))
    for right in range(len(s)):
        window_counter[s[right]] += 1
        if right - left + 1 > len(p):
            window_counter[s[left]] -= 1
            if window_counter[s[left]] == 0:
                del window_counter[s[left]]
            left += 1
        if window_counter == p_counter:
            result.append(left)
    return result


print(findAllAnagram("cbaebabacd", "abc"))
