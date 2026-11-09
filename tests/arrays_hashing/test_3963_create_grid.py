from solutions.arrays_hashing.easy._3963_create_grid import Solution

def test_createGrid():
    solution = Solution()

    assert solution.createGrid(2, 3) in [["...","##."],["..#","#.."]]
    assert solution.createGrid(3, 3) in [["...","##.","##."],["..#","#..","##."]]
    assert solution.createGrid(1, 4) == ["...."]