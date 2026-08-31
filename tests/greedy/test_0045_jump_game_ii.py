from solutions.greedy.medium._0045_jump_game_ii import Solution

def test_jump_game_ii():
    solution = Solution()

    assert solution.jump([2,3,1,1,4]) == 2
    assert solution.jump([2,3,0,1,4]) == 2
