from solutions.graphs.medium._0417_pacific_atlantic_water_flow import Solution

def test_pacific_atlantic_water_flow():
    solution = Solution()

    heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4],
    ]

    result = solution.pacificAtlantic(heights)

    assert {tuple(x) for x in result} == {
        (0,4), (1,3), (1,4), (2,2),
        (3,0), (3,1), (4,0)
    }
