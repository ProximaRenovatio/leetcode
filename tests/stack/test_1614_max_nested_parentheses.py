from solutions.stack.easy._1614_max_nested_parentheses import Solution

def test_maxDepth():
    solution = Solution()

    assert solution.maxDepth("(1+(2*3)+((8)/4))+1") == 3
    assert solution.maxDepth("(1)+((2))+(((3)))") == 3
    assert solution.maxDepth("()(())((()()))") == 3