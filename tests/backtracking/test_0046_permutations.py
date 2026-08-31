from solutions.backtracking.medium._0046_permutations import Solution

def test_permutations():
    solution = Solution()

    result = solution.permute([1,2,3])

    assert {tuple(x) for x in result} == {
        (1,2,3), (1,3,2), (2,1,3),
        (2,3,1), (3,1,2), (3,2,1)
    }
