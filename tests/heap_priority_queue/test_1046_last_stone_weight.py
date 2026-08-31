from solutions.heap_priority_queue.easy._1046_last_stone_weight import Solution

def test_last_stone_weight():
    solution = Solution()

    assert solution.lastStoneWeight([2,7,4,1,8,1]) == 1
    assert solution.lastStoneWeight([1]) == 1
