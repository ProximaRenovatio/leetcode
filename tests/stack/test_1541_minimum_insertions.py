from solutions.stack.medium._1541_minimum_insertions import Solution

def test_minInsertions():
    solution = Solution()

    assert solution.minInsertions("(()))") == 1
    assert solution.minInsertions("())") == 0
    assert solution.minInsertions("(((") == 6
