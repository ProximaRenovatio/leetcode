from solutions.sliding_window.medium._0424_longest_repeating_character_replacement import Solution

def test_longest_repeating_character_replacement():
    solution = Solution()

    assert solution.characterReplacement("ABAB", 2) == 4
    assert solution.characterReplacement("AABABBA", 1) == 4
