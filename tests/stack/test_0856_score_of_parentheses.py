from solutions.stack.medium._0856_score_of_parentheses import Solution as SolutionStack
from solutions.stack.medium._0856_score_of_parentheses_DP import Solution as SolutionDP

def test_score_of_parentheses():

    solution_stack = SolutionStack()
    assert solution_stack.scoreOfParentheses("()") == 1
    assert solution_stack.scoreOfParentheses("(())") == 2
    assert solution_stack.scoreOfParentheses("()()") == 2

    solution_dp = SolutionDP()
    assert solution_dp.scoreOfParentheses("()") == 1
    assert solution_dp.scoreOfParentheses("(())") == 2
    assert solution_dp.scoreOfParentheses("()()") == 2