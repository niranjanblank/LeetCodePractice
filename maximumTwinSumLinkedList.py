"""
2130. Maximum Twin Sum of a Linked List
Medium
Topics
Companies
Hint
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedList(head):

    curr_node = head
    prev_node = None
    next_node = None

    while curr_node:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    return prev_node


def transverse_list(head):
    current = head
    while current:
        print(current.val)
        current = current.next
def maxTwinSum(head):
    slow, fast = head, head

    # find middle of linked list
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next


    second_half = reverseLinkedList(slow)

    max_sum = 0
    while second_half:
        max_sum = max(max_sum, head.val + second_half.val)
        head = head.next
        second_half = second_half.next
    return max_sum

def seperateLinkedList(head):
    n=0
    curr = head
    while curr:
        n+=1
        curr = curr.next

    list_one = head
    list_two = None
    curr = head
    for i in range(int(n/2)+1):

        if i == int(n/2)-1:
            list_two = curr.next
            curr.next = None
            break
        curr = curr.next

    return list_one, list_two

def findMaxTwinSum(list_a, list_b):
    max_sum = 0
    while list_a:
        max_sum = max(max_sum, list_a.val + list_b.val)
        list_a = list_a.next
        list_b = list_b.next
    return max_sum

def method_one(head):
    # this is slower
    list_a, list_b = seperateLinkedList(head)
    list_b = reverseLinkedList(list_b)
    max_sum = findMaxTwinSum(list_a, list_b)
    return max_sum

def method_two(head):
    " This is faster as it uses two pointer "
    max_sum = maxTwinSum(head)
    return max_sum

if __name__ == '__main__':
    head = ListNode(5,ListNode(4,ListNode(2, ListNode(1, None))))
    print(method_two(head))
    # print(method_two(head))


