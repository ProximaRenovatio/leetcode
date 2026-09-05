from solutions.arrays_hashing.medium._3904_smallest_stable_index_ii import Solution

def test_firstStableIndex():
    solution = Solution()

    assert solution.firstStableIndex([5,0,1,4], 3) == 3
    assert solution.firstStableIndex([3,2,1], 1) == -1

    assert solution.firstStableIndex([0], 0) == 0
    assert solution.firstStableIndex([0], 1) == 0

    assert solution.firstStableIndex([1,2], 1) == 0
    assert solution.firstStableIndex([1,1], 1) == 0
    assert solution.firstStableIndex([1,1], 0) == 0
    assert solution.firstStableIndex([1,2], 2) == 0
    assert solution.firstStableIndex([2,4], 0) == 0
    assert solution.firstStableIndex([2,1], 0) == -1
    assert solution.firstStableIndex([2,1], 1) == 0
    assert solution.firstStableIndex([2,1], 2) == 0

    assert solution.firstStableIndex([1,2,3], 0) == 0
    assert solution.firstStableIndex([1,2,3], 1) == 0
    assert solution.firstStableIndex([1,2,3], 2) == 0
    assert solution.firstStableIndex([3,2,1], 0) == -1
    assert solution.firstStableIndex([3,2,1], 1) == -1
    assert solution.firstStableIndex([3,2,1], 2) == 0
    assert solution.firstStableIndex([2,2,2], 0) == 0

    assert solution.firstStableIndex([1,2,3,4], 0) == 0
    assert solution.firstStableIndex([1,1,2,2], 1) == 0
    assert solution.firstStableIndex([1,2,3,4], 1) == 0
    assert solution.firstStableIndex([4,3,2,1], 0) == -1
    assert solution.firstStableIndex([4,3,2,1], 2) == -1
    assert solution.firstStableIndex([1,3,2,4], 0) == 0
    assert solution.firstStableIndex([4,2,3,1], 1) == -1
    assert solution.firstStableIndex([4,2,3,1], 0) == -1