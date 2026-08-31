from solutions.math_geometry.medium._0073_set_matrix_zeroes import Solution

def test_set_matrix_zeroes():
    solution = Solution()

    matrix = [
        [1,1,1],
        [1,0,1],
        [1,1,1],
    ]

    solution.setZeroes(matrix)

    assert matrix == [
        [1,0,1],
        [0,0,0],
        [1,0,1],
    ]
