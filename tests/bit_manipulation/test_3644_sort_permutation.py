from solutions.bit_manipulation.medium._3644_sort_permutation import Solution

def test_sort_permutation():
    solution = Solution()

    assert solution.sortPermutation([0,3,2,1]) == 1
    assert solution.sortPermutation([0,1,3,2]) == 2
    assert solution.sortPermutation([3,2,1,0]) == 0