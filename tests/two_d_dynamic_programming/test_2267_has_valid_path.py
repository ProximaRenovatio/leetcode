from solutions.two_d_dynamic_programming.hard._2267_has_valid_path import Solution

def test_hasValidPath():
    solution = Solution()

    assert solution.hasValidPath([["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]) == True
    assert solution.hasValidPath([[")",")"],["(","("]]) == False