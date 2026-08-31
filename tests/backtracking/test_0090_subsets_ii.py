from solutions.backtracking.medium._0090_subsets_ii import Solution

def test_subsets_ii():
    solution = Solution()

    result = solution.subsetsWithDup([1,2,2])

    assert {tuple(sorted(x)) for x in result} == {
        (), (1,), (2,), (1,2), (2,2), (1,2,2)
    }
