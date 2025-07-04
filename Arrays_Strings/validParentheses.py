# Problem: Valid Parentheses
# Prompt:
# Given a string containing just the characters (, ), {, }, [ and ], determine if the input string is valid.

# A string is valid if:

# Open brackets are closed by the same type of brackets.

# Open brackets are closed in the correct order.

# Every closing bracket has a corresponding open bracket.

# Input: s = "()[]{}"
# Output: True

# Input: s = "(]"
# Output: False

def isValidParentheses(string):
    opening = ['(', '[', '{']
    map = {')': '(', ']': '[', '}': '{'}
    check = []
    for char in string:

        if char in opening:
            check.append(char)
        elif char in map:
            # if check[-1] == map[char]:
            #     check.pop()
            # else:
            #     return False
            if not check or check[-1] != map[char]:
                return False
            check.pop()
    if len(check) == 0:
        return True


print(isValidParentheses("(]"))
