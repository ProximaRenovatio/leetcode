from solutions.strings.medium._0678_valid_parenthesis_string import Solution

def test_convert():
    solution = Solution()

    assert solution.checkValidString("()") == True
    assert solution.checkValidString("(*)*)*)") == True
    assert solution.checkValidString("(*))") == True
    assert solution.checkValidString("(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
) == False
    assert solution.checkValidString(")") == False
    assert solution.checkValidString("*") == True
    assert solution.checkValidString("((((()(()()()*()(((((*)()*(**(())))))(())()())(((())())())))))))(((((())*)))()))(()((*()*(*)))(*)()") == True