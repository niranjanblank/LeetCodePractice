"""
19. Remove Nth Node From End of List
Medium
Topics
Companies
Hint
Given the head of a linked list, remove the nth node from the end of the list and return its head.



Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]


Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

"""
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def multipleReverseSolution(head,n):
    if not head:
        return None

        # Step 1: Reverse the linked list
    prev = None
    curr = head
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    head = prev  # New head of the reversed list

    # Step 2: Remove the nth node from the beginning (since the list is reversed)
    dummy = ListNode(0)  # Create a dummy node
    dummy.next = head
    curr = dummy
    for _ in range(n - 1):
        if curr.next:  # Move to the next node
            curr = curr.next
        else:
            return None  # n is greater than the length of the list
    # Remove the nth node
    curr.next = curr.next.next if curr.next else None

    # Step 3: Reverse the list back to its original order
    prev = None
    curr = dummy.next
    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp

    return prev

def betterSolution(head,n):
    # this solution will keep the distance between left and right pointers to be n, so when right reaches the end of list
    # left would be the node to be deleted
    # we need dummy to delete the left node
    dummy = ListNode()
    dummy.next = head

    left = dummy
    right = head

    # transversing until we reach n
    while n > 0 and right:
        n -= 1
        right = right.next

    # transversing until we reach the end of the list
    while right:
        left = left.next
        right = right.next

    # deleting the node
    left.next = left.next.next

    return dummy.next
