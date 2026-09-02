from solutions.two_d_dynamic_programming.medium._0518_coin_change_ii import Solution

def test_coin_change_ii():
    solution = Solution()

    assert solution.change(5, [1,2,5]) == 4
    assert solution.change(3, [2]) == 0
    assert solution.change(10, [10]) == 1
