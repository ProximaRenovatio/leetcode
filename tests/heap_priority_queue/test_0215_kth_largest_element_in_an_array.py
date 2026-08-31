from solutions.heap_priority_queue.medium._0215_kth_largest_element_in_an_array import Solution

def test_kth_largest_element_in_an_array():
    solution = Solution()

    assert solution.findKthLargest([3,2,1,5,6,4], 2) == 5
    assert solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
