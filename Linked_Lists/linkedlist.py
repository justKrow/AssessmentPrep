# Fill in this function to build a list from [10, 20, 30]

# TODO: create nodes and link them
class listNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list():
    node30 = listNode(30)
    node20 = listNode(20, node30)
    node10 = listNode(10, node20)
    return (node10)


def print_list(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print(None)


print_list(build_list())  # Should print: 10 → 20 → 30 → None
