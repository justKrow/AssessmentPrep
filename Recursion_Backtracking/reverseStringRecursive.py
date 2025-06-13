# "Reverse a String Recursively"
# 📜 Prompt:
# Write a function that reverses a string using recursion (no loops).
# Input: "hello"
# Output: "olleh"

def reverse(word):
    if len(word) <= 1:
        return word
    return reverse(word[1:]) + word[0]


print(reverse("hello"))
