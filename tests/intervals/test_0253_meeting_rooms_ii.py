from solutions.intervals.medium._0253_meeting_rooms_ii import Solution

def test_meeting_rooms_ii():
    solution = Solution()

    assert solution.minMeetingRooms([[0,30],[5,10],[15,20]]) == 2
    assert solution.minMeetingRooms([[7,10],[2,4]]) == 1
