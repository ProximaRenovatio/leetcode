from solutions.greedy.medium._3789_minimum_cost import Solution

def test_minimum_cost():
    solution = Solution()

    assert solution.minCost(3, 2, 1, 3, 2) == 3
    assert solution.minCost(5, 4, 15, 2, 3) == 22
    assert solution.minCost(5, 4, 15, 0, 0) == 0