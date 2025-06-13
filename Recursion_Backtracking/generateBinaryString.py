# Generate All Binary Strings of Length n
# Prompt:
# Given an integer n, generate all binary strings (composed of 0 and 1) of length n.

# For example, if n = 2, the output should be: ["00", "01", "10", "11"]

result = []
def generateBinaryString(n , current):
    if len(current) == n:
        result.append(current)
        return
        
    generateBinaryString(n, current + "0")
    generateBinaryString(n, current + "1")

generateBinaryString(6, "")
print(result)