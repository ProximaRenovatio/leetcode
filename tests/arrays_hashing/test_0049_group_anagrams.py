from solutions.arrays_hashing.medium._0049_group_anagrams import Solution

def test_group_anagrams():
    solution = Solution()

    result = solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(map(sorted, result)) == sorted(
        map(sorted, [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    )

    result = solution.groupAnagrams([""])
    assert result == [[""]]

    result = solution.groupAnagrams(["a"])
    assert result == [["a"]]
