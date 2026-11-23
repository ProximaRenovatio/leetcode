from solutions.math_geometry.medium._0462_min_moves_ii import Solution

def test_minMoves2():
    solution = Solution()

    assert solution.minMoves2([1, 2, 3]) == 2
    assert solution.minMoves2([1, 10, 2, 9]) == 16