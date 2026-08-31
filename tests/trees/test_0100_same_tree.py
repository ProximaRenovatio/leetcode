from solutions.trees.easy._0100_same_tree import Solution

def test_same_tree():
    solution = Solution()

    p = TreeNode(1, TreeNode(2), TreeNode(3))
    q = TreeNode(1, TreeNode(2), TreeNode(3))

    assert solution.isSameTree(p, q) is True
