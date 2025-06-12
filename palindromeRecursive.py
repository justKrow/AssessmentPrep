# Is a String a Palindrome? (Recursive)
# 📜 Prompt:
# Write a function that checks whether a string is a palindrome using recursion.

# A palindrome is a word that reads the same backward and forward.
# Examples: "racecar", "level", "madam"

def isPalindrome(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return isPalindrome(word[1:-1])
    return False


print(isPalindrome("asdasf"))
