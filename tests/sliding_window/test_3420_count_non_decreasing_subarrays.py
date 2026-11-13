from solutions.sliding_window.hard._3420_count_non_decreasing_subarrays import Solution

def test_countNonDecreasingSubarrays():
    solution = Solution()

    assert solution.countNonDecreasingSubarrays([6,3,1,2,4,4], 7) == 17
    assert solution.countNonDecreasingSubarrays([6,3,1,3,6], 4) == 12