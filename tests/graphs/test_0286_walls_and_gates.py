from solutions.graphs.medium._0286_walls_and_gates import Solution

def test_walls_and_gates():
    solution = Solution()

    INF = 2147483647

    grid = [
        [INF, -1, 0, INF],
        [INF, INF, INF, -1],
        [INF, -1, INF, -1],
        [0, -1, INF, INF],
    ]

    solution.islandsAndTreasure(grid)

    assert grid == [
        [3, -1, 0, 1],
        [2, 2, 1, -1],
        [1, -1, 2, -1],
        [0, -1, 3, 4],
    ]
