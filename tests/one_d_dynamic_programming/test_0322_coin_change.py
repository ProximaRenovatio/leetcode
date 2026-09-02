from solutions.one_d_dynamic_programming.medium._0322_coin_change import Solution

def test_coin_change():
    solution = Solution()

    assert solution.coinChange([1,2,5], 11) == 3
    assert solution.coinChange([2], 3) == -1
    assert solution.coinChange([1], 0) == 0
