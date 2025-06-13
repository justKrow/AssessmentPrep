# Problem: Detect a Cycle in a Linked List
# 🧠 Difficulty: Medium
# 📚 Concepts: Linked lists, pointers, Floyd’s Tortoise and Hare algorithm (2-pointer)
# 📝 Prompt:
# Write a function to determine if a linked list contains a cycle.

# A cycle happens when a node's .next points back to a previous node.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head: ListNode) -> bool:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
