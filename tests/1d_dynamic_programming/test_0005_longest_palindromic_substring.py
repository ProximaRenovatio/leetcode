from solutions.1d_dynamic_programming.medium._0005_longest_palindromic_substring import Solution

def test_longest_palindromic_substring():
    solution = Solution()

    assert solution.longestPalindrome("babad") in ("bab", "aba")
    assert solution.longestPalindrome("cbbd") == "bb"
