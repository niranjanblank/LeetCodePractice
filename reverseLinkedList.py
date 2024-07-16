class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseList(head):
    # Initialize three pointers to help in reversing the list:
    # - current_node points to the current node we're examining.
    # - prev_node points to the node that comes before the current node in the reversed list.
    # - next_node temporarily stores the next node to process.
    current_node = head
    prev_node = None
    next_node = None

    # Iterate through the list until we've processed all nodes.
    while current_node:
        # Save the next node since we're going to change current_node's next pointer.
        next_node = current_node.next
        # Reverse the current node's next pointer to point to the previous node.
        current_node.next = prev_node
        # Move prev_node and current_node one step forward in the list.
        # Now, prev_node points to the current node, and current_node moves to next_node.
        prev_node = current_node
        current_node = next_node

    # Once we're done with all nodes, prev_node will be pointing to the new head of the reversed list.
    return prev_node

def transverse_list(head):
    current = head
    while current:
        print(current.value)
        current = current.next




if __name__ == "__main__":
    # Example usage
    head = ListNode(7, ListNode(5, ListNode(3, ListNode(56, ListNode(5)))))
    print("*********Initial Linked List**********")
    transverse_list(head)
    head = reverseList(head)
    print("*********Reversed Linked List**********")
    transverse_list(head)
