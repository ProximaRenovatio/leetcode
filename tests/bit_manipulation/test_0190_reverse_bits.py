from solutions.bit_manipulation.easy._0190_reverse_bits import Solution

def test_reverse_bits():
    solution = Solution()

    assert solution.reverseBits(
        0b00000010100101000001111010011100
    ) == 964176192
