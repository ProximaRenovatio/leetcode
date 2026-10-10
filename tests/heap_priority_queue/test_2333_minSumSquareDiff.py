from solutions.heap_priority_queue.medium._2333_minSumSquareDiff import Solution

def test_min_sum_square_diff():
    solution = Solution()

    assert solution.minSumSquareDiff([1,2,3,4], [2,10,20,19], 0, 0) == 579
    assert solution.minSumSquareDiff([1,4,10,12], [5,8,6,9], 1, 1) == 43
