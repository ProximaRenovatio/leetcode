from solutions.backtracking.medium._0039_combination_sum import Solution

def test_combination_sum():
    solution = Solution()

    result = solution.combinationSum([2,3,6,7], 7)

    assert {tuple(sorted(x)) for x in result} == {(2,2,3), (7,)}
