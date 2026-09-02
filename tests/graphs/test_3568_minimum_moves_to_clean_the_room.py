from solutions.graphs.medium._3568_minimum_moves_to_clean_the_room import Solution

def test_minMoves():
    solution = Solution()

    assert solution.minMoves(["S.", "XL"], 2) == 2
    assert solution.minMoves(["LS", "RL"], 4) == 3
    assert solution.minMoves(["L.S", "RXL"], 3) == -1
    assert solution.minMoves(["SLL", ".XL", "LX."], 7) == 7




    