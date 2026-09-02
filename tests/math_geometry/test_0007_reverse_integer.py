from solutions.math_geometry.medium._0007_reverse_integer import Solution

def test_reverse_integer():
    solution = Solution()

    assert solution.reverse(123)  == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120)  == 21
