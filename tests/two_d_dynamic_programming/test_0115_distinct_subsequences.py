from solutions.two_d_dynamic_programming.hard._0115_distinct_subsequences import Solution

def test_distinct_subsequences():
    solution = Solution()

    assert solution.numDistinct("rabbbit", "rabbit") == 3
    assert solution.numDistinct("babgbag", "bag") == 5
