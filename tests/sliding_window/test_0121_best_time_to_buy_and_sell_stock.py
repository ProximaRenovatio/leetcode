from solutions.sliding_window.easy._0121_best_time_to_buy_and_sell_stock import Solution

def test_best_time_to_buy_and_sell_stock():
    solution = Solution()

    assert solution.maxProfit([7,1,5,3,6,4]) == 5
    assert solution.maxProfit([7,6,4,3,1]) == 0
