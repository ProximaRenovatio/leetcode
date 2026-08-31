from solutions.trees.easy._0226_invert_binary_tree import Solution

def test_invert_binary_tree():
    solution = Solution()

    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(7, TreeNode(6), TreeNode(9))

    result = solution.invertTree(root)

    assert result.val == 4
    assert result.left.val == 7
    assert result.right.val == 2
