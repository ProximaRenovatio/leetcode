from solutions.arrays_hashing.easy._2913_subarrays_distinct_element import Solution

def test_sumCounts():
    solution = Solution()

    assert solution.sumCounts([1,2,1]) == 15
    assert solution.sumCounts([1,1]) == 3