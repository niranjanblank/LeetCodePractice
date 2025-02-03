"""
2046. Sort Linked List Already Sorted Using Absolute Values
Solved
Medium
Topics
Hint
Given the head of a singly linked list that is sorted in non-decreasing order using the absolute values of its nodes, return the list sorted in non-decreasing order using the actual values of its nodes.
 

Example 1:


Input: head = [0,2,-5,5,10,-10]
Output: [-10,-5,0,2,5,10]
Explanation:
The list sorted in non-descending order using the absolute values of the nodes is [0,2,-5,5,10,-10].
The list sorted in non-descending order using the actual values is [-10,-5,0,2,5,10].
Example 2:


Input: head = [0,1,2]
Output: [0,1,2]
Explanation:
The linked list is already sorted in non-decreasing order.
Example 3:

Input: head = [1]
Output: [1]
Explanation:
The linked list is already sorted in non-decreasing order.
 

Constraints:

The number of nodes in the list is the range [1, 105].
-5000 <= Node.val <= 5000
head is sorted in non-decreasing order using the absolute value of its nodes.
 

Follow up:
Can you think of a solution with O(n) time complexity?
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Time Complexity: O(n)
        # Space Complexity: O(1)

        # traverse the linked list
        # set prev to he head and curr be the element after head
        prev, curr = head, head.next
        while curr: 
            if curr.val < 0:
                # if we find a negative value, we break its connectioon
                # and connect prev node to the next node of the curr node
                # add the next of curr node to the head node
                # and set the head to curr
                # set the currr back to temp to continue traversing the linked list
                temp = curr.next
                prev.next = temp  # Remove `curr` from its position
                curr.next = head  # Insert `curr` at the front
                head = curr  # Update head

                # Move `curr` forward correctly to prevent infinite loop
                curr = temp  

            else:
                prev = curr
                curr = curr.next

     
        return head
