from solutions.one_d_dynamic_programming.medium._3524_find_x_value_of_array import Solution

def test_resultArray():
    solution = Solution()

    assert solution.resultArray([1,2,3,4,5], 3) == [9,2,4]
    assert solution.resultArray([1,2,4,8,16,32], 4) == [18,1,2,0]
    assert solution.resultArray([1,1,2,1,1], 2) == [9,6]