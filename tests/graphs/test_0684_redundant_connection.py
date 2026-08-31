from solutions.graphs.medium._0684_redundant_connection import Solution

def test_redundant_connection():
    solution = Solution()

    assert solution.findRedundantConnection(
        [[1,2],[1,3],[2,3]]
    ) == [2,3]
