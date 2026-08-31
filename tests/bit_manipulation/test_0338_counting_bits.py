from solutions.bit_manipulation.easy._0338_counting_bits import Solution

def test_counting_bits():
    solution = Solution()

    assert solution.countBits(2) == [0,1,1]
    assert solution.countBits(5) == [0,1,1,2,1,2]
