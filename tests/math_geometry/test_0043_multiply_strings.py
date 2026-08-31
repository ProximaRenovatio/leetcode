from solutions.math_geometry.medium._0043_multiply_strings import Solution

def test_multiply_strings():
    solution = Solution()

    assert solution.multiply("2", "3") == "6"
    assert solution.multiply("123", "456") == "56088"
    assert solution.multiply("0", "52") == "0"
