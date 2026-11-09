from solutions.heap_priority_queue.hard._1606_busiest_servers import Solution

def test_busiest_servers():
    solution = Solution()

    assert solution.busiestServers(3, [1,2,3,4,5], [5,2,3,3,3]) == [1]
    assert solution.busiestServers(3, [1,2,3,4], [1,2,1,2]) == [0]
    assert solution.busiestServers(3, [1,2,3], [10,12,11]) == [0,1,2]