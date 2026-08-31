from solutions.advanced_graphs.hard._0269_alien_dictionary import Solution

def test_alien_dictionary():
    solution = Solution()

    assert solution.foreignDictionary(
        ["z","o"]
    ) in ("zo", "oz")

    assert solution.foreignDictionary(
        ["hrn","hrf","er","enn","rfnn"]
    ) == "hernf"
