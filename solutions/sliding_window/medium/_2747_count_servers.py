class Solution:
        def countServers(
                self, n: int, logs: list[list[int]], x: int, queries: list[int]
                    ) -> list[int]:

                            logs.sort(key=lambda log: log[1])

                                    sorted_queries = sorted(
                                                (q, i) for i, q in enumerate(queries)
                                                        )

                                                                count = {}
                                                                        res = [0] * len(queries)

                                                                                left = 0
                                                                                        right = 0
                                                                                                active = 0

                                                                                                        for q, idx in sorted_queries:
                                                                                                                    start = q - x

                                                                                                                                # Add logs up to the query time
                                                                                                                                            while right < len(logs) and logs[right][1] <= q:
                                                                                                                                                            server = logs[right][0]

                                                                                                                                                                            if count.get(server, 0) == 0:
                                                                                                                                                                                                active += 1

                                                                                                                                                                                                                count[server] = count.get(server, 0) + 1
                                                                                                                                                                                                                                right += 1

                                                                                                                                                                                                                                            # Remove logs outside the time window
                                                                                                                                                                                                                                                        while left < right and logs[left][1] < start:
                                                                                                                                                                                                                                                                        server = logs[left][0]

                                                                                                                                                                                                                                                                                        count[server] -= 1

                                                                                                                                                                                                                                                                                                        if count[server] == 0:
                                                                                                                                                                                                                                                                                                                            active -= 1
                                                                                                                                                                                                                                                                                                                                                del count[server]

                                                                                                                                                                                                                                                                                                                                                                left += 1

                                                                                                                                                                                                                                                                                                                                                                            res[idx] = n - active

                                                                                                                                                                                                                                                                                                                                                                                    return res