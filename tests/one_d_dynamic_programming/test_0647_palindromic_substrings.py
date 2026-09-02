from solutions.one_d_dynamic_programming.medium._0647_palindromic_substrings import Solution

def test_palindromic_substrings():
    solution = Solution()

    assert solution.countSubstrings("abc") == 3
    assert solution.countSubstrings("aaa") == 6
