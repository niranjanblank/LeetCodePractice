"""

"""
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def deleteMiddle(head):
    if not head.next:
        return head

    # transversing to get the number of nodes
    n = 0
    current = head
    while current:
        n+=1
        current = current.next

    middle_of_list = n//2

    current_prev = None
    current_node = head
    for i in range(middle_of_list):
        current_prev = current_node
        current_node = current_prev.next


    # checking
    if current_prev:
        current_prev.next = current_node.next

    return head


def deleteMiddleBetter(head):
    if head is None or head.next is None:
        return None
    slow, fast = head, head
    prev = None
    # at the end of this node, slow is the middle node
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    prev.next = slow.next

    return head



if __name__ == "__main__":
    # Example usage
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(deleteMiddleBetter(head).value)