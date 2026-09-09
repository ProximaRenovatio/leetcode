from solutions.math_geometry.medium._3871_count_commas_ii import Solution

def test_countCommas():
    solution = Solution()

    assert solution.countCommas(1002) == 3
    assert solution.countCommas(998) == 0
    assert solution.countCommas(1) == 0
    assert solution.countCommas(99999999999999) == 398998998999000
    assert solution.countCommas(1000000000000000) == 3998998998999005
    
  

    