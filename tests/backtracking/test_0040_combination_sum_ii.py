from solutions.backtracking.medium._0040_combination_sum_ii import Solution

def test_combination_sum_ii():
    solution = Solution()

    result = solution.combinationSum2([10,1,2,7,6,1,5], 8)

    assert {tuple(sorted(x)) for x in result} == {
        (1,1,6), (1,2,5), (1,7), (2,6)
    }
