from solutions.2d_dynamic_programming.medium._0309_best_time_to_buy_and_sell_stock_with_cooldown import Solution

def test_best_time_to_buy_and_sell_stock_with_cooldown():
    solution = Solution()

    assert solution.maxProfit([1,2,3,0,2]) == 3
    assert solution.maxProfit([1]) == 0
