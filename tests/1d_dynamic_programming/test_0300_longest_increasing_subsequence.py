from solutions.1d_dynamic_programming.medium._0300_longest_increasing_subsequence import Solution

def test_longest_increasing_subsequence():
    solution = Solution()

    assert solution.lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert solution.lengthOfLIS([0,1,0,3,2,3]) == 4
    assert solution.lengthOfLIS([7,7,7,7,7,7,7]) == 1
