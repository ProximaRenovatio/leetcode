from solutions.arrays_hashing.easy._0242_valid_anagram import Solution

def test_valid_anagram():
    solution = Solution()

    assert solution.isAnagram("anagram", "nagaram") is True
    assert solution.isAnagram("rat", "car") is False
