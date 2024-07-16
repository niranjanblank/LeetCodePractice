class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p,q):
    # check if both nodes are None to terminate recursion
    if p is None and q is None:
        return True
    elif (p is None) or (q is None):
        # check if anyone of them is None and other is not none
        return False
    elif p.val != q.val:
        # check if the values of nodes are different or not
        return False
    else:
        # recursively find if the left and right of both nodes are matching
        left_match = isSameTree(p.left,q.left)
        right_match = isSameTree(p.right, q.right)
        return left_match and right_match


if __name__=="__main__":
    a = TreeNode(1)
    a.left = TreeNode(2)
    a.right = TreeNode(3)

    b = TreeNode(1)
    b.left = TreeNode(4)
    b.right = TreeNode(3)

    print(isSameTree(a,b))

