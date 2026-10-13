from solutions.greedy.medium._3727_max_alternating_sum import Solution

def test_maxAlternatingSum():
    solution = Solution()

    assert solution.maxAlternatingSum([1,2,3]) == 12
    assert solution.maxAlternatingSum([1,-1,2,-2,3,-3]) == 16
