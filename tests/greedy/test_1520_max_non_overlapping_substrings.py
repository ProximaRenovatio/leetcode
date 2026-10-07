from solutions.greedy.hard._1520_max_non_overlapping_substrings import Solution

def test_maxNumOfSubstrings():
    solution = Solution()

    assert solution.maxNumOfSubstrings("adefaddaccc") == ["e","f","ccc"]
    assert solution.maxNumOfSubstrings("abbaccd") == ["bb","cc","d"]

