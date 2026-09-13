from solutions.arrays_hashing.medium._0835_image_overlap import Solution

def test_two_sum():
    solution = Solution()

    assert solution.largestOverlap([[1,1,0],[0,1,0],[0,1,0]], [[0,0,0],[0,1,1],[0,0,1]]) == 3
    assert solution.largestOverlap([[1]], [[1]]) == 1
    assert solution.largestOverlap([[0]], [[0]]) == 0