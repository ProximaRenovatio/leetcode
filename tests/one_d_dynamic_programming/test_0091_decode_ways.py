from solutions.one_d_dynamic_programming.medium._0091_decode_ways import Solution

def test_decode_ways():
    solution = Solution()

    assert solution.numDecodings("12") == 2
    assert solution.numDecodings("226") == 3
    assert solution.numDecodings("06") == 0
