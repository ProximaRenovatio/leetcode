from solutions.two_d_dynamic_programming.hard._0940_distinct_subsequences_ii import Solution

def test_distinct_subsequences():
    solution = Solution()

    assert solution.numDistinct("abc") == 7
    assert solution.numDistinct("aaa") == 3
