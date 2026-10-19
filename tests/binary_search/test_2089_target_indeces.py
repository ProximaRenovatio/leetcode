from solutions.binary_search.easy._2089_target_indices import Solution

def test_target_indices():
    solution = Solution()
    assert solution.targetIndices([1, 2, 5, 2, 3], 2) == [1, 2]
    assert solution.targetIndices([1, 2, 5, 2, 3], 3) == [3]
    assert solution.targetIndices([1, 2, 5, 2, 3], 5) == [4]
