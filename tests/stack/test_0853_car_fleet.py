from solutions.stack.medium._0853_car_fleet import Solution

def test_car_fleet():
    solution = Solution()

    assert solution.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]) == 3
    assert solution.carFleet(10, [3], [3]) == 1
    assert solution.carFleet(100, [0,2,4], [4,2,1]) == 1
