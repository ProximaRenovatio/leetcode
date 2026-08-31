from solutions.greedy.easy._0053_maximum_subarray import Solution

def test_maximum_subarray():
    solution = Solution()

    assert solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert solution.maxSubArray([1]) == 1
    assert solution.maxSubArray([5,4,-1,7,8]) == 23
