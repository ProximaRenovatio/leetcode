from solutions.1d_dynamic_programming.medium._0152_maximum_product_subarray import Solution

def test_maximum_product_subarray():
    solution = Solution()

    assert solution.maxProduct([2,3,-2,4]) == 6
    assert solution.maxProduct([-2,0,-1]) == 0
