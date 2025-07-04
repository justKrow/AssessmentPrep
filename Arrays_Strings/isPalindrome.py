# Write a function that checks if a string is a palindrome, ignoring non-alphanumeric characters and case.

# A palindrome reads the same forward and backward.
# Input: "A man, a plan, a canal: Panama"
# Output: True

# Input: "race a car"
# Output: False

# def isPalindrome(string):
#     string = string.replace(" ", "").replace(
#         ",", "").replace(":", "").replace(".", "").lower()
#     print(string)
#     return string[:] == string[-1::-1]

def isPalindrome(string):
    cleaned = "".join(char.lower() for char in string if char.isalnum())
    return cleaned == cleaned[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))
