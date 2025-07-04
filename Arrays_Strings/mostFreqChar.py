# Write a function that takes a string and returns the character that appears most frequently.

# Example:
# Input: "banana" → Output: "a" (appears 3 times)

from collections import Counter


# def mostFreq(string):
#     freq = Counter(string)
#     for key, value in freq.items():
#         if value == max(freq.values()):
#             return key

def mostFreq(string):
    freq = Counter(string)
    max_count = max(freq.values())
    for key, value in freq.items():
        if value == max_count:
            return key


print(mostFreq("banana"))
