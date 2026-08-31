from solutions.sliding_window.medium._0567_permutation_in_string import Solution

def test_permutation_in_string():
    solution = Solution()

    assert solution.checkInclusion("ab", "eidbaooo") is True
    assert solution.checkInclusion("ab", "eidboaoo") is False
