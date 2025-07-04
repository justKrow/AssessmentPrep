# Given two strings s and t, return True if t is an anagram of s, and False otherwise.

# An anagram means both strings use the same letters the same number of times, just in a different order

# Input: s = "listen", t = "silent"
# Output: True

# Input: s = "hello", t = "bello"
# Output: False

from collections import Counter


# def isAnagram(s, t):
#     s_freq = Counter(s)
#     t_freq = Counter(t)
#     if s_freq == t_freq:
#         return True
#     return False

def isAnagram(s, t):
    return Counter(s) == Counter(t)


print(isAnagram("hello", "bello"))
