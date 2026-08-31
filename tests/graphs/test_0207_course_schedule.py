from solutions.graphs.medium._0207_course_schedule import Solution

def test_course_schedule():
    solution = Solution()

    assert solution.canFinish(2, [[1,0]]) is True
    assert solution.canFinish(2, [[1,0],[0,1]]) is False
