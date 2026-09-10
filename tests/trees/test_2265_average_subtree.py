from solutions.trees.medium._2265_average_subtree import Solution, TreeNode

def test_average_subtree():
    solution = Solution()

    root = TreeNode(4)
    root.left = TreeNode(8, TreeNode(0), TreeNode(1))
    root.right = TreeNode(5, None, TreeNode(6))

    assert solution.averageOfSubtree(root) == 5
