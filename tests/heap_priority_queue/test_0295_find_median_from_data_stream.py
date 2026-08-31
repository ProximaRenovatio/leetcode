from solutions.heap_priority_queue.hard._0295_find_median_from_data_stream import MedianFinder

def test_find_median_from_data_stream():
    finder = MedianFinder()

    finder.addNum(1)
    finder.addNum(2)

    assert finder.findMedian() == 1.5

    finder.addNum(3)

    assert finder.findMedian() == 2.0
