class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def longestZigZag(root):
    def dfs(node, direction, length):
        nonlocal max_length
        if not node:
            return 0
        max_length = max(max_length, length)
        if direction=="left":
            # explore current zigzag path
            dfs(node.left,"right",length+1)
            # explore alternate zigzag path
            dfs(node.right, "left", 1)
        else:
            dfs(node.right, "left", length + 1)
            dfs(node.left, "right",1 )


    max_length = 0
    dfs(root,'left',0)
    # dfs(root, 'right',0)
    return max_length


root = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(1)
root.right.right = TreeNode(1)
root.right.right.left = TreeNode(1)
root.right.right.right = TreeNode(1)
root.right.right.left.right = TreeNode(1)
root.right.right.left.right.right = TreeNode(1)

print(longestZigZag(root))