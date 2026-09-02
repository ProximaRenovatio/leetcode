from solutions.two_d_dynamic_programming.medium._0494_target_sum import Solution

def test_target_sum():
    solution = Solution()

    assert solution.findTargetSumWays([1,1,1,1,1], 3) == 5
    assert solution.findTargetSumWays([1], 1) == 1
