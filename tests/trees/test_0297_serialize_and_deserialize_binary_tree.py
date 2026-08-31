from solutions.trees.hard._0297_serialize_and_deserialize_binary_tree import Codec

def test_serialize_and_deserialize_binary_tree():
    codec = Codec()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3, TreeNode(4), TreeNode(5))

    encoded = codec.serialize(root)
    decoded = codec.deserialize(encoded)

    assert decoded.val == 1
    assert decoded.left.val == 2
    assert decoded.right.val == 3
    assert decoded.right.left.val == 4
    assert decoded.right.right.val == 5
