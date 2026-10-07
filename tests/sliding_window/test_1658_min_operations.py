from solutions.sliding_window.medium._1658_min_operations import Solution

def test_minOperations():
    solution = Solution()

    assert solution.minOperations([1,1,4,2,3], 5) == 2
    assert solution.minOperations([5,6,7,8,9], 4) == -1
    assert solution.minOperations([3,2,20,1,1,3], 10) == 5