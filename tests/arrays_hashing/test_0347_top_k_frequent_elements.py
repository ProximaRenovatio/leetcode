from solutions.arrays_hashing.medium._0347_top_k_frequent_elements import Solution

def test_top_k_frequent_elements():
    solution = Solution()

    assert set(solution.topKFrequent([1, 1, 1, 2, 2, 3], 2)) == {1, 2}
    assert solution.topKFrequent([1], 1) == [1]
