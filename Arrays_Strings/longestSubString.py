# Given a string s, find the length of the longest substring without repeating characters.

# 🔍 Why this matters:
# Common in string manipulation problems.

# Requires understanding hash maps + two-pointer technique.
# Input: "abcabcbb"
# Output: 3
# Explanation: The longest substring without repeating characters is "abc".

# Input: "bbbbb"
# Output: 1

# Input: "pwwkew"
# Output: 3  # ("wke")

def longestSubString(string):
    # map = {}
    # i = 0
    # max_count = 0
    # for j in range(0, len(string)):
    #     if string[j] not in map:
    #         map[string[j]] = j
    #     else:
    #         i = j
    #     print(string[i:j+1])
    #     max_count = max(max_count, len(string[i:j+1]))
    # return max_count
    map = {}
    left = 0
    max_count = 0
    for right in range(len(string)):
        if string[right] in map and left <= map[string[right]]:
            left = map[string[right]] + 1

        map[string[right]] = right
        max_count = max(max_count, right - left + 1)
    return max_count


print(longestSubString("pwwkew"))
