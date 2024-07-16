class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1, root2):
        tree1_leaf = self.getLeafNodes(root1)
        tree2_leaf = self.getLeafNodes(root2)
        return tree1_leaf==tree2_leaf

    def getLeafNodes(self,node):
        leafNodes = []

        if node is not None:

            if node.left is None and node.right is None:
                leafNodes.append(node.val)
            else:
                left_node = self.getLeafNodes(node.left)
                right_node = self.getLeafNodes(node.right)
                leafNodes.extend(left_node)
                leafNodes.extend(right_node)
        return leafNodes

# Helper function to build a tree from a list of values (for simplicity)
def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    nodes = [root]
    i = 1
    while i < len(values):
        node = nodes.pop(0)
        if node:
            node.left = TreeNode(values[i]) if values[i] is not None else None
            nodes.append(node.left)
            if i + 1 < len(values):
                node.right = TreeNode(values[i + 1]) if values[i + 1] is not None else None
                nodes.append(node.right)
                i += 1
        i += 1
    return root

sol = Solution()

# Test case 1: Identical trees
tree1 = build_tree([3,5,1,6,2,9,8,None,None,7,4])
tree2 = build_tree([3,5,1,6,2,9,8,None,None,7,4])
assert sol.leafSimilar(tree1, tree2) == True, "Test case 1 failed"

# Test case 2: Same leaves, different structure
# Revised Test case 2: Same leaves, different structure, but leaves are in the same sequence
tree1 = build_tree([1,2,3,4,None,None,5])  # Tree structure:   1
                                           #                  / \
                                           #                 2   3
                                           #                /
                                           #               4
                                           #                \
                                           #                 5
tree2 = build_tree([1,2,3,None,4,None,5])  # Tree structure:   1
                                           #                  / \
                                           #                 2   3
                                           #                  \
                                           #                   4
                                           #                    \
                                           #                     5
assert sol.leafSimilar(tree1, tree2) == True, "Revised Test case 2 failed"

# Test case 3: Different leaves
tree1 = build_tree([1,2,4])
tree2 = build_tree([1,2,3])
assert sol.leafSimilar(tree1, tree2) == False, "Test case 3 failed"

# Test case 4: One or both trees are empty
tree1 = build_tree([])
tree2 = build_tree([1,2,3])
assert sol.leafSimilar(tree1, tree2) == False, "Test case 4 failed"
assert sol.leafSimilar(tree2, tree1) == False, "Test case 4 failed"
assert sol.leafSimilar(tree1, tree1) == True, "Test case 4 failed"

# Test case 5: Trees with only one node each
tree1 = build_tree([1])
tree2 = build_tree([1])
assert sol.leafSimilar(tree1, tree2) == True, "Test case 5 failed"

print("All test cases passed!")