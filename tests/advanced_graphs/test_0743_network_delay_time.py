from solutions.advanced_graphs.medium._0743_network_delay_time import Solution

def test_network_delay_time():
    solution = Solution()

    assert solution.networkDelayTime(
        [[2,1,1],[2,3,1],[3,4,1]],
        4,
        2,
    ) == 2

    assert solution.networkDelayTime([[1,2,1]], 2, 1) == 1
    assert solution.networkDelayTime([[1,2,1]], 2, 2) == -1
