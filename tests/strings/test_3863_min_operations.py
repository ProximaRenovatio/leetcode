from solutions.strings.medium._3863_min_operations import Solution

def test_minOperations():
    solution = Solution()

    assert solution.minOperations("dog") == 1
    assert solution.minOperations("card") == 2
    assert solution.minOperations("gf") == -1