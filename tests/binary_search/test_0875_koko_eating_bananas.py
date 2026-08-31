from solutions.binary_search.medium._0875_koko_eating_bananas import Solution

def test_koko_eating_bananas():
    solution = Solution()

    assert solution.minEatingSpeed([3,6,7,11], 8) == 4
    assert solution.minEatingSpeed([30,11,23,4,20], 5) == 30
    assert solution.minEatingSpeed([30,11,23,4,20], 6) == 23
