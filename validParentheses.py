# Given a string containing just the characters (, ), {, }, [ and ], determine if the input string is valid.

# A string is valid if:

# Open brackets must be closed by the same type of brackets.

# Open brackets must be closed in the correct order.

# Every closing bracket must have a corresponding open bracket.

def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '[', '}': '{'}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
        else:
            return False
    return not stack


print(is_valid("([{])"))
