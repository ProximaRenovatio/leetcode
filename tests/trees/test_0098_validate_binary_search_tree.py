from solutions.trees.medium._0098_validate_binary_search_tree import Solution

def test_validate_binary_search_tree():
    solution = Solution()

    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert solution.isValidBST(root) is True

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4, TreeNode(3), TreeNode(6))

    assert solution.isValidBST(root) is False
