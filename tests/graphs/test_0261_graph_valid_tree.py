from solutions.graphs.medium._0261_graph_valid_tree import Solution

def test_graph_valid_tree():
    solution = Solution()

    assert solution.validTree(
        5,
        [[0,1],[0,2],[0,3],[1,4]],
    ) is True

    assert solution.validTree(
        5,
        [[0,1],[1,2],[2,3],[1,3],[1,4]],
    ) is False
