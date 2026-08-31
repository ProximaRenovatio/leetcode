from solutions.two_pointers.medium._0015_3sum import Solution

def test_3sum():
    solution = Solution()

    result = solution.threeSum([-1, 0, 1, 2, -1, -4])
    assert sorted(map(sorted, result)) == [[-1, -1, 2], [-1, 0, 1]]

    assert solution.threeSum([0, 1, 1]) == []
    assert solution.threeSum([0, 0, 0]) == [[0, 0, 0]]
