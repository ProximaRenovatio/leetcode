from solutions.sliding_window.hard._0076_minimum_window_substring import Solution

def test_minimum_window_substring():
    solution = Solution()

    assert solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert solution.minWindow("a", "a") == "a"
    assert solution.minWindow("a", "aa") == ""
