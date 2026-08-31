from solutions.bit_manipulation.medium._0007_reverse_integer import Solution

def test_reverse_integer():
    solution = Solution()

    assert solution.reverse(123) == 321
    assert solution.reverse(-123) == -321
    assert solution.reverse(120) == 21
    assert solution.reverse(1534236469) == 0
