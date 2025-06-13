# Problem: "Valid Anagram"
# Prompt:
# Given two strings s and t, return True if t is an anagram of s, and False otherwise.
# (An anagram is a word formed by rearranging the letters of another, using all the original letters exactly once.)
# Input: s = "anagram", t = "nagaram"
# Output: True

# Input: s = "rat", t = "car"
# Output: False

from collections import Counter

def isAnagramCounter(s,t):
    s_map = Counter(s)
    t_map = Counter(t)
    
    if s_map == t_map:
        return True
    return False

def isAnagramNoCounter(s,t):
    if len(s) != len(t):
        return False
    freq_s = {}
    freq_t = {}

    for char in s:
        freq_s[char] = freq_s.get(char, 0) + 1

    for char in t:
        freq_t[char] = freq_t.get(char, 0) + 1
    
    return freq_s == freq_t
    

print(isAnagramNoCounter("aabb","baaa"))