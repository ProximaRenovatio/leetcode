from solutions.stack.medium._1190_reverse_parentheses import Solution

def test_reverseParentheses():
    solution = Solution()

    assert solution.reverseParentheses("(abcd)") == "dcba"
    assert solution.reverseParentheses("(u(love)i)") == "iloveu"
    assert solution.reverseParentheses("(ed(et(oc))el)") == "leetcode"
