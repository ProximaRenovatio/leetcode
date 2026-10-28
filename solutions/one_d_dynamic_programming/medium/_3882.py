
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
            m, n = len(grid), len(grid[0])

                    # dp[j] stores the XOR values reachable at the current row
                            dp = [set() for _ in range(n)]
                                    dp[0].add(grid[0][0])

                                            for i in range(m):
                                                        for j in range(n):
                                                                        if i == 0 and j == 0:
                                                                                            continue

                                                                                                            current = set()

                                                                                                                            # Reach this cell from above
                                                                                                                                            if i > 0:
                                                                                                                                                                for x in dp[j]:
                                                                                                                                                                                        current.add(x ^ grid[i][j])

                                                                                                                                                                                                        # Reach this cell from the left
                                                                                                                                                                                                                        if j > 0:
                                                                                                                                                                                                                                            for x in dp[j - 1]:
                                                                                                                                                                                                                                                                    current.add(x ^ grid[i][j])

                                                                                                                                                                                                                                                                                    dp[j] = current

                                                                                                                                                                                                                                                                                            return min(dp[n - 1])
                                                                                                                                                                                                                                                                                            