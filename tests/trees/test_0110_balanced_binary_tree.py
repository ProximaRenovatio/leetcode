from solutions.trees.easy._0110_balanced_binary_tree import Solution

def test_balanced_binary_tree():
    solution = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    assert solution.isBalanced(root) is True

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)

    assert solution.isBalanced(root) is False
