# Preorder	4 2 1 3 6 5 7	Root → Left → Right
# Inorder	1 2 3 4 5 6 7	Left → Root → Right
# Postorder	1 3 2 5 7 6 4	Left → Right → Root


class treeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def inOrder(node):
    if not node:
        return
    inOrder(node.left)
    print(node.val, end=" ")
    inOrder(node.right)


def preOrder(node):
    if not node:
        return
    print(node.val, end=" ")
    preOrder(node.left)
    preOrder(node.right)


def postOrder(node):
    if not node:
        return
    postOrder(node.left)
    postOrder(node.right)
    print(node.val, end=" ")


root = treeNode(1)
root.left = treeNode(2)
root.right = treeNode(3)
root.left.left = treeNode(4)
root.left.right = treeNode(5)


inOrder(root)
print("")
preOrder(root)
print("")
postOrder(root)
