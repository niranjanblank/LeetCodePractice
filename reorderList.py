"""
143. Reorder List
Medium
Topics
Companies
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.



Example 1:


Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:


Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]


Constraints:

The number of nodes in the list is in the range [1, 5 * 104].
1 <= Node.val <= 1000
"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reorderList(head):
    # finding the middle of the list using the fast and slow method
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # setting the head of the 2nd list
    second_curr = slow.next
    # detaching the 2nd part of the list
    slow.next = None

    # reversing the 2nd list
    prev = None

    while second_curr:
        # storing the broken link
        tmp = second_curr.next
        second_curr.next = prev
        prev = second_curr
        second_curr = tmp

    # getting the heads of the two lists
    first, second = head, prev

    # merging the lists
    # choosing second as length of second might be smaller than first
    while second:
        # storing the broken links of first and second
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        # transversing the lists
        first = tmp1
        second = tmp2
