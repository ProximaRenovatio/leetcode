from solutions.math_geometry.medium._3876_uniform_array_ii import Solution

def test_uniform_array():
    solution = Solution()

    assert solution.uniformArray([2, 3]) == False
    assert solution.uniformArray([4, 6]) == True