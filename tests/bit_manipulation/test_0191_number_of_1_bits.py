from solutions.bit_manipulation.easy._0191_number_of_1_bits import Solution

def test_number_of_1_bits():
    solution = Solution()

    assert solution.hammingWeight(11) == 3
    assert solution.hammingWeight(128) == 1
