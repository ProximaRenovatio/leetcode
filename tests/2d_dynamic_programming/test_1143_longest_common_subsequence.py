from solutions.2d_dynamic_programming.medium._1143_longest_common_subsequence import Solution

def test_longest_common_subsequence():
    solution = Solution()

    assert solution.longestCommonSubsequence("abcde", "ace") == 3
    assert solution.longestCommonSubsequence("abc", "abc") == 3
    assert solution.longestCommonSubsequence("abc", "def") == 0
