from solutions.greedy.medium._3723_max_sum_of_square import Solution

def test_max_sum_of_square():
    solution = Solution()

    assert solution.maxSumOfSquares(2, 3) == "30"
    assert solution.maxSumOfSquares(2, 17) == "98"
    assert solution.maxSumOfSquares(1, 10) == ""