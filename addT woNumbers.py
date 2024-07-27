"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.



Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


Constraints:

The number of nodes in each linked list is in the range [1, 100].
"""

# method 1
def addTwoNumbers(l1, l2):
    num1 = 0
    multiplier = 1
    num2 = 0

    # getting num1 from l1
    curr = l1
    while curr:
        num1 += multiplier * curr.val
        curr = curr.next
        multiplier *= 10

    # getting num2 from l2
    multiplier = 1
    curr = l2
    while curr:
        num2 += multiplier * curr.val
        curr = curr.next
        multiplier *= 10

    # summing and converting to str for creating easier linked list
    sum_num = str(num1 + num2)[::-1]

    prev = ListNode(int(sum_num[0]))
    head = prev
    for i in range(1, len(sum_num)):
        curr = ListNode(int(sum_num[i]))
        prev.next = curr
        prev = curr

    return head

# method 2

def addTwoNumbers2(l1,l2):
    dummy = ListNode()
    curr = dummy

    carry = 0

    while l1 or l2 or carry:
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0

        # getting the sum of the v1 and v2 digits
        val = v1 + v2 + carry

        # getting the carry
        carry = val // 10

        # getting the last place digit
        val = val % 10

        # creating the node
        curr.next = ListNode(val)

        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next