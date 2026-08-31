from solutions.math_geometry.medium._0202_happy_number import Solution

def test_happy_number():
    solution = Solution()

    assert solution.isHappy(19) is True
    assert solution.isHappy(2) is False
