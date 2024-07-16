class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def searchBST(root, val):
    # Base case: root is null or the value of root is the value we are searching for.
    if root is None or root.val == val:
        return root

    # If the value to search is smaller than the root's value,
    # then it lies in the left subtree.
    if val < root.val:
        return searchBST(root.left, val)

    # Otherwise, the value lies in the right subtree.
    return searchBST(root.right, val)


if __name__== '__main__':
    # Creating nodes
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node7 = TreeNode(7)

    # Creating root and setting up the tree structure
    root = TreeNode(2, node1, node3)
    node3.right = node4
    node4.right = node7

    print(searchBST(root,7).val)