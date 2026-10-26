from solutions.arrays_hashing.medium._3619_count_islands import Solution

def test_countIslands():
    solution = Solution()

    # Test case 1
    grid1 = [
        [0,2,1,0,0],
        [0,5,0,0,5],
        [0,0,1,0,0],
        [0,1,4,7,0],
        [0,2,0,0,8]
    ]
    assert solution.countIslands(grid1, 5) == 2

    # Test case 2
    grid2 = [
        [3,0,3,0],
        [0,3,0,3],
        [3,0,3,0]
    ]
    assert solution.countIslands(grid2, 3) == 6
    