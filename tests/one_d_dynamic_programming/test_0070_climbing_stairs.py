from solutions.one_d_dynamic_programming.easy._0070_climbing_stairs import Solution

def test_climbing_stairs():
    solution = Solution()

    assert solution.climbStairs(1) == 1
    assert solution.climbStairs(2) == 2
    assert solution.climbStairs(3) == 3
    assert solution.climbStairs(7) == 21
    assert solution.climbStairs(10) == 89
    assert solution.climbStairs(29) == 832040
    assert solution.climbStairs(39) == 102334155
    assert solution.climbStairs(45) == 1836311903