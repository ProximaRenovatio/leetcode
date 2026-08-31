from solutions.two_pointers.hard._0042_trapping_rain_water import Solution

def test_trapping_rain_water():
    solution = Solution()

    assert solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6
    assert solution.trap([4,2,0,3,2,5]) == 9
