from solutions.1d_dynamic_programming.medium._0198_house_robber import Solution

def test_house_robber():
    solution = Solution()

    assert solution.rob([1,2,3,1]) == 4
    assert solution.rob([2,7,9,3,1]) == 12
