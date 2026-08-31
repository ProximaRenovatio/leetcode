from solutions.backtracking.medium._0017_letter_combinations_of_a_phone_number import Solution

def test_letter_combinations_of_a_phone_number():
    solution = Solution()

    result = solution.letterCombinations("23")

    assert len(result) == 9
    assert "ad" in result
    assert "cf" in result

    assert solution.letterCombinations("") == []
