# Happy Number"
# 📜 Prompt:
# A number is called "happy" if repeatedly replacing it by the sum of the squares of its digits eventually leads to 1.

# If it loops forever without hitting 1, it's not a happy number.

# 🧪 Example:
# Input: 19
# 19 → 1² + 9² = 82
# 82 → 8² + 2² = 68
# 68 → 6² + 8² = 100
# 100 → 1² + 0² + 0² = 1 ✅

# Output: True


def isHappy(num):
    seen = set()

    while num != 1:
        if num in seen:
            return False
        seen.add(num)
        num = sum(int(digit)**2 for digit in str(num))
    return True


print(isHappy(19))  # True
print(isHappy(4))   # False
