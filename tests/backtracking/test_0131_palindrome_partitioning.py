from solutions.backtracking.medium._0131_palindrome_partitioning import Solution

def test_palindrome_partitioning():
    solution = Solution()

    result = solution.partition("aab")

    assert {tuple(x) for x in result} == {
        ("a", "a", "b"),
        ("aa", "b"),
    }
