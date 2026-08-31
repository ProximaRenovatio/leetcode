from solutions.trees.medium._0199_binary_tree_right_side_view import Solution

def test_binary_tree_right_side_view():
    solution = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2, None, TreeNode(5))
    root.right = TreeNode(3, None, TreeNode(4))

    assert solution.rightSideView(root) == [1, 3, 4]
