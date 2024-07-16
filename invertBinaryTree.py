class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertBinarytree(root):
    if root is None:
        return None

    # swap left and right children of
    root.left, root.right = root.right, root.left

    # recursively invert the children
    invertBinarytree(root.left)
    invertBinarytree(root.right)

    return root


if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    invertBinarytree(root)
    print(root.left.val)
    print(root.right.val)