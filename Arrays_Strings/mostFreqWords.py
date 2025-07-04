# You're given a list of words. Return the word that appears most frequently.

# If there’s a tie, return any one of the most frequent words.
# Input: ["apple", "banana", "apple", "orange", "banana", "apple"]
# Output: "apple"

from collections import Counter


def mostFreq(words):
    freq = Counter(words)
    return max(freq, key=freq.get)


print(mostFreq(["apple", "banana", "apple", "orange", "banana", "apple"]))
