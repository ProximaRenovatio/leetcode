from solutions.2d_dynamic_programming.hard._0312_burst_balloons import Solution

def test_burst_balloons():
    solution = Solution()

    assert solution.maxCoins([3,1,5,8]) == 167
    assert solution.maxCoins([1,5]) == 10
