from solutions.graphs.medium._0323_number_of_connected_components_in_an_undirected_graph import Solution

def test_number_of_connected_components_in_an_undirected_graph():
    solution = Solution()

    assert solution.countComponents(5, [[0,1],[1,2],[3,4]]) == 2
    assert solution.countComponents(5, []) == 5
