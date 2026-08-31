from solutions.trees.easy._0543_diameter_of_binary_tree import Solution

def test_diameter_of_binary_tree():
    solution = Solution()

    root = TreeNode(1)
    root.right = TreeNode(2, TreeNode(3), TreeNode(4))
    root.right.left.left = TreeNode(5)

    assert solution.diameterOfBinaryTree(root) == 3
