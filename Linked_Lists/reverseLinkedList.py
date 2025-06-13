# Linked List Variant: Reverse a Linked List
# Difficulty: Medium
# Concepts: Linked lists, pointers

# Prompt:
# Write a function that reverses a singly linked list and returns the new head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    # Your code here
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev


def print_list(head):
    while head:
        print(head.val, end='->')
        head = head.next
    print(None)


# Helper to build the list
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
head = node1

# Example Input: 1 → 2 → 3 → None
# Output: 3 → 2 → 1 → None
# Assuming reverse_list is implemented correctly
reversed_head = reverse_list(head)
print_list(reversed_head)
