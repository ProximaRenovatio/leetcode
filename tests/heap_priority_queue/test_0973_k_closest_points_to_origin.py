from solutions.heap_priority_queue.medium._0973_k_closest_points_to_origin import Solution

def test_k_closest_points_to_origin():
    solution = Solution()

    result = solution.kClosest([[1,3],[-2,2]], 1)
    assert result == [[-2,2]]

    result = solution.kClosest([[3,3],[5,-1],[-2,4]], 2)
    assert {tuple(point) for point in result} == {(3,3), (-2,4)}
