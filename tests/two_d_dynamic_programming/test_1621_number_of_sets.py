from solutions.two_d_dynamic_programming.medium._1621_number_of_sets import Solution

def test_numberOfSets():
    solution = Solution()

    assert solution.numberOfSets(4,2) == 5
    assert solution.numberOfSets(3,1) == 3
    assert solution.numberOfSets(30,7) == 796297179