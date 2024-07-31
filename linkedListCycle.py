"""

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# method 1
# O(n) memory
def hasCycle(head):
    items = set()

    while head:
        if head not in items:
            items.add(head)
        if head.next in items:
            return True
        head = head.next
    return False

# method 2 : constant memory
# using tortoise and hare problem with O(1) memory
def hasCycle(head):
    # Initialize two pointers, fast and slow, both pointing to the head of the list
    fast, slow = head, head

    # Traverse the list with the fast pointer moving two steps at a time and the slow pointer moving one step at a time
    while fast and fast.next:
        slow = slow.next  # Move the slow pointer one step forward
        fast = fast.next.next  # Move the fast pointer two steps forward

        # If the fast pointer and the slow pointer meet, there is a cycle in the list
        if fast == slow:
            return True

    # If the fast pointer reaches the end of the list, there is no cycle
    return False