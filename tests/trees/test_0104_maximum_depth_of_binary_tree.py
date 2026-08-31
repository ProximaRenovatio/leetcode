from solutions.trees.easy._0104_maximum_depth_of_binary_tree import Solution

def test_maximum_depth_of_binary_tree():
    solution = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))

    assert solution.maxDepth(root) == 3
