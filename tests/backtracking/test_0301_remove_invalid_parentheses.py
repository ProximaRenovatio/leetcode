from solutions.backtracking.hard._0301_remove_invalid_parentheses import Solution

def test_removeInvalidParentheses():
    solution = Solution()

    assert sorted(solution.removeInvalidParentheses("()())()")) == sorted(["(())()", "()()()"])
    assert sorted(solution.removeInvalidParentheses("(a)())()")) == sorted(["(a())()","(a)()()"])
    assert sorted(solution.removeInvalidParentheses(")(")) == sorted([""])
    
