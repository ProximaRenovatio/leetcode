from solutions.tries.hard._0212_word_search_ii import Solution

def test_word_search_ii():
    solution = Solution()

    board = [
        ["o","a","a","n"],
        ["e","t","a","e"],
        ["i","h","k","r"],
        ["i","f","l","v"],
    ]

    result = solution.findWords(
        board,
        ["oath", "pea", "eat", "rain"],
    )

    assert set(result) == {"oath", "eat"}
