from solutions.2d_dynamic_programming.hard._0329_longest_increasing_path_in_a_matrix import Solution

def test_longest_increasing_path_in_a_matrix():
    solution = Solution()

    assert solution.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]) == 4
    assert solution.longestIncreasingPath([[3,4,5],[3,2,6],[2,2,1]]) == 4
