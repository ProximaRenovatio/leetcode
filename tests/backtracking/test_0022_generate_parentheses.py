from solutions.backtracking.medium._0022_generate_parentheses import Solution

def test_generate_parentheses():
    solution = Solution()

    assert set(solution.generateParenthesis(3)) == {
        "((()))", "(()())", "(())()", "()(())", "()()()"
    }

    assert solution.generateParenthesis(1) == ["()"]
