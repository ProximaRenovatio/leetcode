from solutions.2d_dynamic_programming.hard._0010_regular_expression_matching import Solution

def test_regular_expression_matching():
    solution = Solution()

    assert solution.isMatch("aa", "a") is False
    assert solution.isMatch("aa", "a*") is True
    assert solution.isMatch("ab", ".*") is True
