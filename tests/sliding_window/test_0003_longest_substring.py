from solutions.sliding_window.medium._0003_longest_substring_DICT import Solution

def test_longest_substring():
    solution = Solution()

    assert solution.lengthOfLongestSubstring("abcabcbb") == 3
    assert solution.lengthOfLongestSubstring("bbbbb") == 1
    assert solution.lengthOfLongestSubstring("pwwkew") == 3
    assert solution.lengthOfLongestSubstring("baaabca") == 3
    assert solution.lengthOfLongestSubstring("cdcda") == 3