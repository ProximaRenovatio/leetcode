from solutions.1d_dynamic_programming.medium._0139_word_break import Solution

def test_word_break():
    solution = Solution()

    assert solution.wordBreak("leetcode", ["leet","code"]) is True
    assert solution.wordBreak("applepenapple", ["apple","pen"]) is True
    assert solution.wordBreak("catsandog", ["cats","dog","sand","and","cat"]) is False
