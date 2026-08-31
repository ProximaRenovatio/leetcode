from solutions.math_geometry.easy._0066_plus_one import Solution

def test_plus_one():
    solution = Solution()

    assert solution.plusOne([1,2,3]) == [1,2,4]
    assert solution.plusOne([4,3,2,1]) == [4,3,2,2]
    assert solution.plusOne([9]) == [1,0]
