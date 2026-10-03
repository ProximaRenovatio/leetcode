from solutions.stack.hard._0032_longest_valid_parentheses import Solution

def test_valid_parentheses():
    solution = Solution()

    assert solution.longestValidParentheses("(()") == 2
    assert solution.longestValidParentheses(")()())") == 4
    assert solution.longestValidParentheses("") == 0