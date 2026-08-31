from solutions.sliding_window.medium._0003_longest_substring_without_repeating_characters import Solution

def test_longest_substring_without_repeating_characters():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
