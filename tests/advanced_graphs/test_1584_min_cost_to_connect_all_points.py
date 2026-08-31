from solutions.advanced_graphs.medium._1584_min_cost_to_connect_all_points import Solution

def test_min_cost_to_connect_all_points():
    solution = Solution()

    assert solution.minCostConnectPoints(
        [[0,0],[2,2],[3,10],[5,2],[7,0]]
    ) == 20

    assert solution.minCostConnectPoints(
        [[3,12],[-2,5],[-4,1]]
    ) == 18
