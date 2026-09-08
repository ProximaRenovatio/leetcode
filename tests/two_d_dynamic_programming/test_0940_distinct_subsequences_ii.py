from solutions.two_d_dynamic_programming.hard._0940_distinct_subsequences_ii import Solution

def test_distinct_subsequences():
    solution = Solution()

    assert solution.distinctSubseqII("abc") == 7
    assert solution.distinctSubseqII("aba") == 6
    assert solution.distinctSubseqII("aaa") == 3