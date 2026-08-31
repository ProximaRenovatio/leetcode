from solutions.trees.medium._0102_binary_tree_level_order_traversal import Solution

def test_binary_tree_level_order_traversal():
    solution = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    assert solution.levelOrder(root) == [[3], [9, 20], [15, 7]]
