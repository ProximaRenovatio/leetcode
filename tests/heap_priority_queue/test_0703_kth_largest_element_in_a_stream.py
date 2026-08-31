from solutions.heap_priority_queue.easy._0703_kth_largest_element_in_a_stream import KthLargest

def test_kth_largest_element_in_a_stream():
    kth = KthLargest(3, [4, 5, 8, 2])

    assert kth.add(3) == 4
    assert kth.add(5) == 5
    assert kth.add(10) == 5
    assert kth.add(9) == 8
    assert kth.add(4) == 8
