"""
21. Merge Two Sorted Lists
Easy
Topics
Companies
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.



Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    dummy = ListNode()
    tail = dummy

    # while there are values in both the linked lists
    while list1 and list2:
        # checking which list item has lower value
        if list1.val < list2.val:
            tail.next = list1
            # transverse through the linked list
            list1 = list1.next
        else:
            tail.next = list2
            # transverse through the linked list
            list2 = list2.next

        # transverse through the merged list we are creating
        tail = tail.next

    # if list1 still has some values left
    if list1:
        tail.next = list1
    elif list2:
    # if list 2 still has some values left
        tail.next = list2

    return dummy.next


    return dummy.next