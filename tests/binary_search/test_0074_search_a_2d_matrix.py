from solutions.binary_search.medium._0074_search_a_2d_matrix import Solution

def test_search_a_2d_matrix():
    solution = Solution()

    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60],
    ]

    assert solution.searchMatrix(matrix, 3) is True
    assert solution.searchMatrix(matrix, 13) is False
