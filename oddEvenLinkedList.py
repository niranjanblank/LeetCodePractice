class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next

def offEvenList(head):
    if not head:
        return head

    # using two pointers
    odd = head
    even = head.next
    evenHead = even
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next

    odd.next = evenHead
    return head