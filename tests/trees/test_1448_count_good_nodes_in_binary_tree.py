from solutions.trees.medium._1448_count_good_nodes_in_binary_tree import Solution

def test_count_good_nodes_in_binary_tree():
    solution = Solution()

    root = TreeNode(3)
    root.left = TreeNode(1, TreeNode(3))
    root.right = TreeNode(4, TreeNode(1), TreeNode(5))

    assert solution.goodNodes(root) == 4
