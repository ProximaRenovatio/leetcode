from solutions.graphs.medium._1267_count_servers import Solution

def test_count_servers():
    solution = Solution()

    assert solution.countServers([[1,0],[0,1]]) == 0
    assert solution.countServers([[1,0],[1,1]]) == 3
    assert solution.countServers([[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]) == 4
