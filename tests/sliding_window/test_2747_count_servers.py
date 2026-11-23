from solutions.sliding_window.medium._1658_min_operations import Solution

def test_minOperations():
    solution = Solution()

    assert solution.minOperations(3,[[1,3],[2,6],[1,5]], 5, [10,11]) == [1,2]
