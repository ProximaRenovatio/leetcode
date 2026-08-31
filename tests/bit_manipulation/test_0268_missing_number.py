from solutions.bit_manipulation.easy._0268_missing_number import Solution

def test_missing_number():
    solution = Solution()

    assert solution.missingNumber([3,0,1]) == 2
    assert solution.missingNumber([0,1]) == 2
    assert solution.missingNumber([9,6,4,2,3,5,7,0,1]) == 8
