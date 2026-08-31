from solutions.trees.medium._0230_kth_smallest_element_in_a_bst import Solution

def test_kth_smallest_element_in_a_bst():
    solution = Solution()

    root = TreeNode(3)
    root.left = TreeNode(1, None, TreeNode(2))
    root.right = TreeNode(4)

    assert solution.kthSmallest(root, 1) == 1
    assert solution.kthSmallest(root, 3) == 3
