# ✅ Problem: Partition Labels
# 🧠 Category: Greedy + HashMap/String

# 🔍 Prompt:
# You are given a string s.
# You want to partition the string into as many parts as possible
# so that each letter appears in at most one part.

# Return a list of integers representing the size of these parts.
# Input: "ababcbacadefegdehijhklij"
# Output: [9,7,8]

# Explanation:
# - The first partition is "ababcbaca" → All `a, b, c`
# - Then "defegde" → All `d, e, f, g`
# - Then "hijhklij" → All `h, i, j, k, l`

def partitionLabels(s):
    last = {ch: idx for idx, ch in enumerate(s)}  # Step 1
    print(last)
    partitions = []
    start = end = 0

    for i, ch in enumerate(s):
        end = max(end, last[ch])  # Extend the window
        if i == end:  # Partition point
            partitions.append(end - start + 1)
            start = i + 1  # Move start

    return partitions


print(partitionLabels("ababcbacadefegdehijhklij"))
