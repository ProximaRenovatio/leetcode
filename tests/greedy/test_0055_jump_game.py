from solutions.greedy.medium._0055_jump_game import Solution

def test_jump_game():
    solution = Solution()

    assert solution.canJump([2,3,1,1,4]) is True
    assert solution.canJump([3,2,1,0,4]) is False
