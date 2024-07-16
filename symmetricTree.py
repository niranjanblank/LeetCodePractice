class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def symmetric(root):
    if root is None:
        return True

    def isMirror(left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val != right.val:
            return False
        else:
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)

    return isMirror(root.left, root.right)




if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    invertBinarytree(root)
    print(root.left.val)
    print(root.right.val)