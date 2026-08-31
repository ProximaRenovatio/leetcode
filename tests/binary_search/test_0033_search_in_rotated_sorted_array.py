from solutions.binary_search.medium._0033_search_in_rotated_sorted_array import Solution

def test_search_in_rotated_sorted_array():
    solution = Solution()

    assert solution.search([4,5,6,7,0,1,2], 0) == 4
    assert solution.search([4,5,6,7,0,1,2], 3) == -1
    assert solution.search([1], 0) == -1
