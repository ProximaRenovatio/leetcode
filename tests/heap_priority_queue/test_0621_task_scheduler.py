from solutions.heap_priority_queue.medium._0621_task_scheduler import Solution

def test_task_scheduler():
    solution = Solution()

    assert solution.leastInterval(["A","A","A","B","B","B"], 2) == 8
    assert solution.leastInterval(["A","A","A","B","B","B"], 0) == 6
