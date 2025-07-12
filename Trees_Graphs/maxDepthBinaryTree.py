# 🧩 Problem: Maximum Depth of Binary Tree
# 📄 Description:
# Given the root of a binary tree, return its maximum depth.

# The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Input:
#         3
#        / \
#       9  20
#          / \
#         15  7

# Output: 3
# Explanation: Path = 3 → 20 → 15 (or 3 → 20 → 7)

class treeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


root = treeNode(1)
root.left = treeNode(3)
root.right = treeNode(5)
root.left.left = treeNode(2)

print(maxDepth(root))
