from solutions.graphs.medium._0133_clone_graph import Solution

def test_clone_graph():
    solution = Solution()

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)

    node1.neighbors = [node2, node4]
    node2.neighbors = [node1, node3]
    node3.neighbors = [node2, node4]
    node4.neighbors = [node1, node3]

    clone = solution.cloneGraph(node1)

    assert clone is not node1
    assert clone.val == 1
    assert sorted(n.val for n in clone.neighbors) == [2, 4]
