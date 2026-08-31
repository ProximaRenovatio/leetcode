from solutions.backtracking.medium._0079_word_search import Solution

def test_word_search():
    solution = Solution()

    board = [
        ["A","B","C","E"],
        ["S","F","C","S"],
        ["A","D","E","E"],
    ]

    assert solution.exist(board, "ABCCED") is True
    assert solution.exist(board, "SEE") is True
    assert solution.exist(board, "ABCB") is False
