from solutions.1d_dynamic_programming.easy._0746_min_cost_climbing_stairs import Solution

def test_min_cost_climbing_stairs():
    solution = Solution()

    assert solution.minCostClimbingStairs([10,15,20]) == 15
    assert solution.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]) == 6
