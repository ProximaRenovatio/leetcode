from solutions.intervals.easy._0252_meeting_rooms import Solution

def test_meeting_rooms():
    solution = Solution()

    assert solution.canAttendMeetings([[0,30],[5,10],[15,20]]) is False
    assert solution.canAttendMeetings([[7,10],[2,4]]) is True
