from solutions.math_geometry.medium._1401_circle_rectangle_overlapping import Solution

def test_checkOverlap():
    solution = Solution()

    assert solution.checkOverlap(1,0,0,1,-1,3,1) is True
    assert solution.checkOverlap(1,1,1,1,-3,2,-1) is False
    assert solution.checkOverlap(1,0,0,-1,0,0,1) is True
