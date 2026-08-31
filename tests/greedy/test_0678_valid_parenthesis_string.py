from solutions.greedy.medium._0678_valid_parenthesis_string import Solution

def test_valid_parenthesis_string():
    solution = Solution()

    assert solution.checkValidString("()") is True
    assert solution.checkValidString("(*)") is True
    assert solution.checkValidString("(*))") is True
    assert solution.checkValidString(")(") is False
