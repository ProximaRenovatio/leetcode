from solutions.intervals.medium._1851_minimum_interval_to_include_each_query import Solution

def test_minimum_interval_to_include_each_query():
    solution = Solution()

    assert solution.minInterval(
        [[1,4],[2,4],[3,6],[4,4]],
        [2,3,4,5],
    ) == [3,3,1,4]
