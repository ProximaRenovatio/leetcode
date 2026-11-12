from solutions.arrays_hashing.easy._3105_longest_monotonic_subarray import Solution

def test_longestMonotonicSubarray():
    solution = Solution()

    assert solution.longestMonotonicSubarray([1,4,3,3,2]) == 2
    assert solution.longestMonotonicSubarray([3,3,3,3]) == 1
    assert solution.longestMonotonicSubarray([3,2,1]) == 3