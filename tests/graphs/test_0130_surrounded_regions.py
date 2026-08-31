from solutions.graphs.medium._0130_surrounded_regions import Solution

def test_surrounded_regions():
    solution = Solution()

    board = [
        ["X","X","X","X"],
        ["X","O","O","X"],
        ["X","X","O","X"],
        ["X","O","X","X"],
    ]

    solution.solve(board)

    assert board == [
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","X","X","X"],
        ["X","O","X","X"],
    ]
