from solutions.graphs.medium._0210_course_schedule_ii import Solution

def test_course_schedule_ii():
    solution = Solution()

    result = solution.findOrder(2, [[1,0]])

    assert result in ([0,1], [0,1])

    assert solution.findOrder(2, [[1,0],[0,1]]) == []
