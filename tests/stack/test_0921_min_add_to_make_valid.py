from solutions.stack.medium._0921_min_add_to_make_valid import Solution

def test_minAddToMakeValid():
    solution = Solution()

    assert solution.minAddToMakeValid("()()()))((())())(())((())())()())))(())())(()(()(((((())))))))))))))))))))))))))(((((((((((((((((()") == 41
    assert solution.minAddToMakeValid("(((") == 3
    assert solution.minAddToMakeValid(")") == 1
    assert solution.minAddToMakeValid(")))))(") == 6
    assert solution.minAddToMakeValid(")()(") == 2
    assert solution.minAddToMakeValid(")()((()((") == 5
    assert solution.minAddToMakeValid("(((((()))))))()())))()()()()()()())))))((()))((())))((())))))(((()(()()()(((((((((((((((((((((((((((") == 44
    assert solution.minAddToMakeValid("(") == 1