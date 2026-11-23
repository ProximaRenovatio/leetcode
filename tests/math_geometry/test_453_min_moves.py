from solutions.math_geometry.medium._0453_min_moves import Solution

def test_minMoves():
    solution = Solution()

    assert solution.minMoves([1, 2, 3]) == 3
    assert solution.minMoves([1, 1, 1]) == 0