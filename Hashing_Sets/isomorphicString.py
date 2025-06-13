# "Isomorphic Strings"
# 📜 Prompt:
# Given two strings s and t, determine if they are isomorphic.

# Two strings are isomorphic if characters in s can be replaced to get t, with a one-to-one mapping.
# Input: s = "egg", t = "add"
# Output: True

# Input: s = "foo", t = "bar"
# Output: False

def isIsomorphic(s, t):
    if len(s) != len(t):
        return False

    maps_to_t = {}
    mapped_chars = set()

    for i, char_s in enumerate(s):
        char_t = t[i]
        if char_s in maps_to_t:
            if maps_to_t[char_s] != char_t:
                return False
        else:
            if char_t in mapped_chars:
                return False
            maps_to_t[char_s] = char_t
            mapped_chars.add(char_t)
    return True


s = "egg"
t = "add"
print(isIsomorphic(s, t))
