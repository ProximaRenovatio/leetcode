from solutions.2d_dynamic_programming.medium._0062_unique_paths import Solution

def test_unique_paths():
    solution = Solution()

    assert solution.uniquePaths(3, 7) == 28
    assert solution.uniquePaths(3, 2) == 3
