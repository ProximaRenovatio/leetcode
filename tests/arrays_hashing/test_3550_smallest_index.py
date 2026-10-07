from solutions.arrays_hashing.easy._3550_smallest_index import Solution

def test_smallestIndex():
    solution = Solution()

    assert solution.smallestIndex([1,3,2]) == 2
    assert solution.smallestIndex([1,10,11]) == 1
    assert solution.smallestIndex([1,2,3]) == -1