from solutions.trees.medium._0235_lowest_common_ancestor_of_a_binary_search_tree import Solution

def test_lowest_common_ancestor_of_a_binary_search_tree():
    solution = Solution()

    root = TreeNode(6)
    root.left = TreeNode(2, TreeNode(0), TreeNode(4))
    root.right = TreeNode(8, TreeNode(7), TreeNode(9))

    p = root.left
    q = root.right

    assert solution.lowestCommonAncestor(root, p, q).val == 6
