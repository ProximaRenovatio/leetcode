from solutions.2d_dynamic_programming.medium._0097_interleaving_string import Solution

def test_interleaving_string():
    solution = Solution()

    assert solution.isInterleave("aabcc", "dbbca", "aadbbcbcac") is True
    assert solution.isInterleave("aabcc", "dbbca", "aadbbbaccc") is False
