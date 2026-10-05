from solutions.stack.medium._0856_score_of_parentheses import Solution

def test_score_of_parentheses():
    solution = Solution()

    assert solution.scoreOfParentheses("()") == 1
    assert solution.scoreOfParentheses("(())") == 2
    assert solution.scoreOfParentheses("()()") == 2