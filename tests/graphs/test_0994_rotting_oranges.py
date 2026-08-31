from solutions.graphs.medium._0994_rotting_oranges import Solution

def test_rotting_oranges():
    solution = Solution()

    assert solution.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]) == 4
    assert solution.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]) == -1
    assert solution.orangesRotting([[0,2]]) == 0
