from solutions.one_d_dynamic_programming.medium._0213_house_robber_ii import Solution

def test_house_robber_ii():
    solution = Solution()

    assert solution.rob([2,3,2]) == 3
    assert solution.rob([1,2,3,1]) == 4
    assert solution.rob([1,2,3]) == 3
