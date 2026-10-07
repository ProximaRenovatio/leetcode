from solutions.backtracking.hard._1096_brace_expansion_ii import Solution

def test_braceExpansionII():
    solution = Solution()

    assert solution.braceExpansionII("{a,b}{c,{d,e}}") == ["ac","ad","ae","bc","bd","be"]
    assert solution.braceExpansionII("{{a,z},a{b,c},{ab,z}}") == ["a","ab","ac","z"]
