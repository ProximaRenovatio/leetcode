from solutions.math_geometry.hard._3886_sum_of_sortable_integers import Solution

def test_sum_of_sortable_integers():
    solution = Solution()

    assert solution.sortableIntegers([3,1,2]) == 3
    assert solution.sortableIntegers([7,6,5]) == 0
    assert solution.sortableIntegers([5,8]) == 3
