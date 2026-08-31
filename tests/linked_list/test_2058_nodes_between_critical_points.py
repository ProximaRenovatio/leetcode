from solutions.linked_list.medium._2058_nodes_between_critical_points import Solution
from utils.linked_list import *

def test_nodes_between_critical_points():
    solution = Solution()

    assert solution.nodesBetweenCriticalPoints(create_linked_list([5,3,1,2,5,1,2])) == [1, 3]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,1])) == [-1,-1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,2])) == [-1,-1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([2,1,1,2])) == [-1,-1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,2,1])) == [-1,-1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,2,1,2])) == [1, 1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([2,1,3,1,3])) == [1, 2]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,1])) == [-1,-1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,2])) == [-1,-1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([2,1])) == [-1,-1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,3,2,2,3,2,2,2,7])) == [3,3]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1])) == [-1,-1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,3,1,2,3,4,5,6,7])) == [1,1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,3,1,2,3,4,5,6,7])) == [1,1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,1,1,2,3,4,5,6,7])) == [-1,-1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,1,1,2,3,4,5,6,5])) == [-1,-1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,1,1,2,3,4,5,4,5])) == [1,1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,1,1,2,3,4,5,5,4,5])) == [-1,-1]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,1,1,2,3,4,3,3,5,5,4,5])) == [5,5]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,2,1,2,1,4,5,5,4,5])) == [1,7]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,3,1,2,3,4,5,6,5])) == [1,6]
    assert solution.nodesBetweenCriticalPoints(create_linked_list([1,7,3,9,5,12,5,11,7])) == [1,6]
