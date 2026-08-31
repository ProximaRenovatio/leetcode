from solutions.stack.hard._0084_largest_rectangle_in_histogram import Solution

def test_largest_rectangle_in_histogram():
    solution = Solution()

    assert solution.largestRectangleArea([2,1,5,6,2,3]) == 10
    assert solution.largestRectangleArea([2,4]) == 4
