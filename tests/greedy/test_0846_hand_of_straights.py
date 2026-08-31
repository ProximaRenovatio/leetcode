from solutions.greedy.medium._0846_hand_of_straights import Solution

def test_hand_of_straights():
    solution = Solution()

    assert solution.isNStraightHand([1,2,3,6,2,3,4,7,8], 3) is True
    assert solution.isNStraightHand([1,2,3,4,5], 4) is False
