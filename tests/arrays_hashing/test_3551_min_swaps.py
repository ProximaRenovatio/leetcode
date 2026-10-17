from solutions.arrays_hashing.medium._3551_min_swaps import Solution

def test_minSwaps():
    solution = Solution()

    assert solution.minSwaps([37,100]) == 1
    assert solution.minSwaps([22,14,33,7]) == 0
    assert solution.minSwaps([18,43,34,16]) == 2