from solutions.math_geometry.easy._2409_cound_days_together import Solution

def test_count_days_together():
    solution = Solution()

    assert solution.countDaysTogether("08-01", "08-15", "08-10", "08-20") == 6
    assert solution.countDaysTogether("10-01", "10-31", "11-01", "11-30") == 0
    assert solution.countDaysTogether("01-01", "12-31", "06-01", "06-30") == 30
