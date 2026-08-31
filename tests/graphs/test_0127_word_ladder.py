from solutions.graphs.hard._0127_word_ladder import Solution

def test_word_ladder():
    solution = Solution()

    assert solution.ladderLength(
        "hit",
        "cog",
        ["hot","dot","dog","lot","log","cog"],
    ) == 5

    assert solution.ladderLength(
        "hit",
        "cog",
        ["hot","dot","dog","lot","log"],
    ) == 0
