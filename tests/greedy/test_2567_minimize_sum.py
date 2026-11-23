from solutions.greedy.medium._2567_minimize_sum import Solution

def test_minimize_sum():
    solution = Solution()

    assert solution.minimizeSum([1,4,7,8,5]) == 3
    assert solution.minimizeSum([1,4,3]) == 0
