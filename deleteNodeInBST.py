class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_minimum(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode( root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = deleteNode(root.left, key)

    elif key > root.val:
        root.right = deleteNode(root.right, key)

    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        temp = find_minimum(root.right)

        root.val = temp.val

        root.right = deleteNode(root.right, temp.val)
    return root
# Simple inorder traversal to display the BST
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)

if __name__ == '__main__':
    # Create nodes
    root = TreeNode(50)
    root.left = TreeNode(30)
    root.right = TreeNode(70)
    root.left.left = TreeNode(20)
    root.left.right = TreeNode(40)
    root.right.left = TreeNode(60)
    root.right.right = TreeNode(80)
    print('before')
    inorder_traversal(root)
    deleteNode(root,70)
    print('after')
    inorder_traversal(root)