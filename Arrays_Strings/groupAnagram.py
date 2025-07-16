# Input: ["eat","tea","tan","ate","nat","bat"]
# Output: [["eat","tea","ate"],["tan","nat"],["bat"]]

from collections import defaultdict


def sortWord(word):
    return ("".join(sorted(word)))


def groupAnagram(words):
    map = defaultdict(list)
    for word in words:
        sorted_word = sortWord(word)
        print(sorted_word)
        # if sorted_word not in map:
        #     map[sorted_word].append(word)

        # else:
        #     map[sorted_word].append(word)
        map[sorted_word].append(word)
    return list(map.values())


print(groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
