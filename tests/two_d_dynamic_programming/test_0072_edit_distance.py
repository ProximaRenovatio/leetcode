from solutions.two_d_dynamic_programming.hard._0072_edit_distance import Solution

def test_edit_distance():
    solution = Solution()

    assert solution.minDistance("horse", "ros") == 3
    assert solution.minDistance("intention", "execution") == 5
