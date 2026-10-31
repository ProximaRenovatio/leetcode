
class Solution:
    def uniquePaths(self, grid: list[list[int]]) -> int:
            MOD = 10**9 + 7
                    m, n = len(grid), len(grid[0])

                            dp = [1] + [0] * (n - 1)

                                    for i in range(m):
                                                left = 0

                                                            for j in range(n):
                                                                            if grid[i][j] == 1:
                                                                                                # A mirror swaps the two incoming directions
                                                                                                                    left, dp[j] = dp[j], left
                                                                                                                                    else:
                                                                                                                                                        # An empty cell allows both directions
                                                                                                                                                                            left = (left + dp[j]) % MOD
                                                                                                                                                                                                dp[j] = left

                                                                                                                                                                                                        return left
                                                                                                                                                                                                        