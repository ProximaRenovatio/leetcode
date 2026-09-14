from solutions.math_geometry.easy._0836_rectangle_overlap import Solution

def test_happy_number():
    solution = Solution()

    assert solution.isRectangleOverlap([0,0,2,2],[1,1,3,3]) is True
    assert solution.isRectangleOverlap([0,0,1,1],[1,0,2,1]) is False
    assert solution.isRectangleOverlap([0,0,1,1],[2,2,3,3]) is False
    assert solution.isRectangleOverlap([5,15,8,18],[0,3,7,9]) is False
    assert solution.isRectangleOverlap([0,0,1,1],[0,0,1,1]) is True

