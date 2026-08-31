from solutions.intervals.medium._0435_non_overlapping_intervals import Solution

def test_non_overlapping_intervals():
    solution = Solution()

    assert solution.eraseOverlapIntervals(
        [[1,2],[2,3],[3,4],[1,3]]
    ) == 1

    assert solution.eraseOverlapIntervals(
        [[1,2],[1,2],[1,2]]
    ) == 2
