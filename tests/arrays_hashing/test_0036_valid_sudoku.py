from solutions.arrays_hashing.medium._0036_valid_sudoku import Solution

def test_valid_sudoku():
    solution = Solution()

    board = [
        ["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"],
    ]

    assert solution.isValidSudoku(board) is True

    board[0][0] = "8"
    assert solution.isValidSudoku(board) is False
