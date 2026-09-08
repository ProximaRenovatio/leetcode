from solutions.math_geometry.easy._3870_count_commas import Solution

def test_countCommas():
    solution = Solution()

    assert solution.uniformArray(1002) == 3
    assert solution.uniformArray(998) == 0