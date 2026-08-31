from solutions.backtracking.medium._0078_subsets import Solution

def test_subsets():
    solution = Solution()

    result = solution.subsets([1,2,3])
    assert {tuple(sorted(x)) for x in result} == {
        (), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)
    }

    assert solution.subsets([0]) == [[], [0]]
