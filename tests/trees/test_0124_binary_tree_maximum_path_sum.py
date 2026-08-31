from solutions.trees.hard._0124_binary_tree_maximum_path_sum import Solution

def test_binary_tree_maximum_path_sum():
    solution = Solution()

    root = TreeNode(-10)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    assert solution.maxPathSum(root) == 42
