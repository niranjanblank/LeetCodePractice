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


class SolutionBFS:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # if we envounter tree with none, we return None
        if not root:
            return None


        # BFS is implemented using queue
        # we visit each nodes level by level
        queue = deque([root])

        while queue:
            current = queue.popleft()

            current.left, current.right = current.right, current.left

            # add the left or right node to queue if they arent none
            if current.left: queue.append(current.left)
            if current.right: queue.append(current.right)

        return root

if __name__=="__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    invertBinarytree(root)
    print(root.left.val)
    print(root.right.val)