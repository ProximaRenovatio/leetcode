from solutions.graphs.medium._0200_number_of_islands import Solution

def test_number_of_islands():
    solution = Solution()

    grid = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"],
    ]

    assert solution.numIslands(grid) == 1
