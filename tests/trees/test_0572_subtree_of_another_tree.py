from solutions.trees.easy._0572_subtree_of_another_tree import Solution

def test_subtree_of_another_tree():
    solution = Solution()

    root = TreeNode(3)
    root.left = TreeNode(4, TreeNode(1), TreeNode(2))
    root.right = TreeNode(5)

    sub_root = TreeNode(4, TreeNode(1), TreeNode(2))

    assert solution.isSubtree(root, sub_root) is True
