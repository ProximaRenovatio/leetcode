from solutions.advanced_graphs.hard._0778_swim_in_rising_water import Solution

def test_swim_in_rising_water():
    solution = Solution()

    assert solution.swimInWater([[0,2],[1,3]]) == 3
    assert solution.swimInWater([
        [0,1,2,3,4],
        [24,23,22,21,5],
        [12,13,14,15,16],
        [11,17,18,19,20],
        [10,9,8,7,6],
    ]) == 16
