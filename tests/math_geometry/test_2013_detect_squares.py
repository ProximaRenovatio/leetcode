from solutions.math_geometry.hard._2013_detect_squares import DetectSquares

def test_detect_squares():
    squares = DetectSquares()

    squares.add([3,10])
    squares.add([11,2])
    squares.add([3,2])
    assert squares.count([11,10]) == 1

    squares.add([11,2])
    assert squares.count([11,10]) == 2
