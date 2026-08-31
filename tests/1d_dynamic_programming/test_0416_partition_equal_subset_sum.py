from solutions.1d_dynamic_programming.medium._0416_partition_equal_subset_sum import Solution

def test_partition_equal_subset_sum():
    solution = Solution()

    assert solution.canPartition([1,5,11,5]) is True
    assert solution.canPartition([1,2,3,5]) is False
