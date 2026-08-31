from solutions.advanced_graphs.medium._0787_cheapest_flights_within_k_stops import Solution

def test_cheapest_flights_within_k_stops():
    solution = Solution()

    assert solution.findCheapestPrice(
        4,
        [[0,1,100],[1,2,100],[2,3,100],[0,3,500]],
        0,
        3,
        1,
    ) == 500

    assert solution.findCheapestPrice(
        4,
        [[0,1,100],[1,2,100],[2,3,100],[0,3,500]],
        0,
        3,
        2,
    ) == 300
