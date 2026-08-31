from solutions.backtracking.hard._0051_n_queens import Solution

def test_n_queens():
    solution = Solution()

    result = solution.solveNQueens(4)

    assert len(result) == 2
    assert all(len(board) == 4 for board in result)
