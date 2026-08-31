from solutions.stack.medium._0150_evaluate_reverse_polish_notation import Solution

def test_evaluate_reverse_polish_notation():
    solution = Solution()

    assert solution.evalRPN(["2","1","+","3","*"]) == 9
    assert solution.evalRPN(["4","13","5","/","+"]) == 6
    assert solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
