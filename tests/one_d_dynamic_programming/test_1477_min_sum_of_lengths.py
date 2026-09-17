from solutions.one_d_dynamic_programming.medium._1477_min_sum_of_lengths import Solution

def test_minSumOfLengths():
    solution = Solution()

    assert solution.minSumOfLengths([3,2,2,4,3],3) == 2
    assert solution.minSumOfLengths([7,3,4,7], 7) == 2
    assert solution.minSumOfLengths([4,3,2,6,2,3,4], 6) == -1
