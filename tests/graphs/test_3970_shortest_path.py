from solutions.graphs.medium._3970_shortest_path import Solution

def test_shortestPath():
    solution = Solution()

    assert solution.shortestPath(3, [[0,1,1],[1,2,1],[0,2,3]], "aab", 1) == 3
    assert solution.shortestPath(3, [[0,1,1],[1,2,1],[0,2,3]], "aab", 2) == 2
    assert solution.shortestPath(3, [[0,1,1],[1,2,1]], "aaa", 2) == -1
