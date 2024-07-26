"""

Code


Testcase
Test Result
Test Result
138. Copy List with Random Pointer
Medium
Topics
Companies
Hint
A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

Return the head of the copied linked list.

The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.
Your code will only be given the head of the original linked list.



Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]


Constraints:

0 <= n <= 1000
-104 <= Node.val <= 104
Node.random is null or is pointing to some node in the linked list.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    # Initialize a hashmap to store the mapping from original nodes to their deep copies.
    # Include a mapping for None to handle null pointers.
    copy_hashmap = {None: None}

    # First pass: create a deep copy of each node and populate the hashmap.
    curr = head
    while curr:
        # Create a new node with the same value as the current node.
        copy = Node(curr.val)
        # Map the current node to its copy in the hashmap.
        copy_hashmap[curr] = copy
        # Move to the next node in the original list.
        curr = curr.next

    # Second pass: establish the next and random pointers for the copied nodes using the hashmap.
    curr = head
    while curr:
        # Retrieve the copied node from the hashmap.
        copy = copy_hashmap[curr]
        # Set the next pointer of the copied node to the copied next node.
        copy.next = copy_hashmap[curr.next]
        # Set the random pointer of the copied node to the copied random node.
        copy.random = copy_hashmap[curr.random]
        # Move to the next node in the original list.
        curr = curr.next

    # Return the head of the copied linked list.
    return copy_hashmap[head]