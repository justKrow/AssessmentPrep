# Problem: Remove Duplicates from a Sorted Linked List
# 📚 Difficulty: Easy–Medium
# 🧠 Concepts: Linked lists, pointers, conditionals
# 📝 Prompt:
# You're given the head of a sorted linked list. Remove all duplicates in-place so that each element appears only once.

# Return the modified list.

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_duplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head


def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


head = build_linked_list([1, 1, 2, 3, 3])
print("Before removing duplicates:")
print_list(head)
new_head = delete_duplicates(head)

print("After removing duplicates:")
print_list(new_head)
