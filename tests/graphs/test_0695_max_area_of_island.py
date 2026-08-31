from solutions.graphs.medium._0695_max_area_of_island import Solution

def test_max_area_of_island():
    solution = Solution()

    grid = [
        [0,0,0,0,0,0,0,0],
        [0,1,1,1,0,0,0,0],
        [0,1,1,1,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]

    assert solution.maxAreaOfIsland(grid) == 6
