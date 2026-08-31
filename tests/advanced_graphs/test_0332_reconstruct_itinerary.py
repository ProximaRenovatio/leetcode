from solutions.advanced_graphs.hard._0332_reconstruct_itinerary import Solution

def test_reconstruct_itinerary():
    solution = Solution()

    assert solution.findItinerary(
        [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    ) == ["JFK","MUC","LHR","SFO","SJC"]
