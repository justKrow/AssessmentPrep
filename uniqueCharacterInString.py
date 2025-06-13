# First Unique Character in a String
# Difficulty: Easy → Medium
# Concepts: Hash maps (dictionaries), string traversal
# Input: s = "leetcode"
# Output: 0  # 'l' is the first unique character

# Input: s = "loveleetcode"
# Output: 2  # 'v' is the first unique

# Input: s = "aabb"
# Output: -1  # no unique characters

from collections import Counter

def findFirstUniqueChar(word):
    count = Counter(word)
    for i, char in enumerate(word):
        if count[char] == 1:
            return char
    return -1


print(findFirstUniqueChar("loveleetcode"))