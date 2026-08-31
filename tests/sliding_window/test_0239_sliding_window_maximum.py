from solutions.sliding_window.hard._0239_sliding_window_maximum import Solution

def test_sliding_window_maximum():
    solution = Solution()

    assert solution.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert solution.maxSlidingWindow([1], 1) == [1]
