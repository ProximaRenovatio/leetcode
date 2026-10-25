from solutions.arrays_hashing.medium._1254_number_of_closed_islands_MY import Solution as MY
from solutions.arrays_hashing.medium._1254_number_of_closed_islands_DFS import Solution as DFS

def test_closed_island():
    solution1 = MY()
    solution2 = DFS()

    assert solution1.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]) == 2
    assert solution1.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]) == 1
    assert solution1.closedIsland([[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]) == 2

    assert solution2.closedIsland([[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]) == 2
    assert solution2.closedIsland([[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]) == 1
    assert solution2.closedIsland([[1,1,1,1,1,1,1],[1,0,0,0,0,0,1],[1,0,1,1,1,0,1],[1,0,1,0,1,0,1],[1,0,1,1,1,0,1],[1,0,0,0,0,0,1],[1,1,1,1,1,1,1]]) == 2
