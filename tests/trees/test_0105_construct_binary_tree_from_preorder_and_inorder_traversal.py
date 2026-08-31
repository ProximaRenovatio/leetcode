from solutions.trees.medium._0105_construct_binary_tree_from_preorder_and_inorder_traversal import Solution

def test_construct_binary_tree_from_preorder_and_inorder_traversal():
    solution = Solution()

    root = solution.buildTree(
        [3, 9, 20, 15, 7],
        [9, 3, 15, 20, 7],
    )

    assert root.val == 3
    assert root.left.val == 9
    assert root.right.val == 20
