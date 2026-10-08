from solutions.strings.easy._1021_remove_outermost_parentheses import Solution

def test_removeOuterParentheses():
    solution = Solution()

    assert solution.removeOuterParentheses("(()())(())") == "()()()"
    assert solution.removeOuterParentheses("(()())(())(()(()))") == "()()()()(())"
    assert solution.removeOuterParentheses("()()") == ""