from solutions.math_geometry.medium._0050_pow_x_n import Solution

def test_pow_x_n():
    solution = Solution()

    assert solution.myPow(2.0, 10) == 1024.0
    assert solution.myPow(2.1, 3) == 9.261
    assert solution.myPow(2.0, -2) == 0.25
