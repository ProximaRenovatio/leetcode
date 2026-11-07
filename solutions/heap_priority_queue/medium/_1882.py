import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
            available = [(weight, i) for i, weight in enumerate(servers)]
                    heapq.heapify(available)

                            busy = []
                                    res = []
                                            time = 0

                                                    for j, duration in enumerate(tasks):
                                                                # Time cannot go backwards
                                                                            time = max(time, j)

                                                                                        # Release servers that have finished
                                                                                                    while busy and busy[0][0] <= time:
                                                                                                                    free_time, weight, index = heapq.heappop(busy)
                                                                                                                                    heapq.heappush(available, (weight, index))

                                                                                                                                                # If no server is available, wait
                                                                                                                                                            if not available:
                                                                                                                                                                            time = busy[0][0]

                                                                                                                                                                                            # Release all servers available at this time
                                                                                                                                                                                                            while busy and busy[0][0] <= time:
                                                                                                                                                                                                                                free_time, weight, index = heapq.heappop(busy)
                                                                                                                                                                                                                                                    heapq.heappush(available, (weight, index))

                                                                                                                                                                                                                                                                # Select server with minimum weight, then minimum index
                                                                                                                                                                                                                                                                            weight, index = heapq.heappop(available)
                                                                                                                                                                                                                                                                                        res.append(index)

                                                                                                                                                                                                                                                                                                    # Update server's finishing time
                                                                                                                                                                                                                                                                                                                heapq.heappush(
                                                                                                                                                                                                                                                                                                                                busy,
                                                                                                                                                                                                                                                                                                                                                (time + duration, weight, index)
                                                                                                                                                                                                                                                                                                                                                            )

                                                                                                                                                                                                                                                                                                                                                                    return res