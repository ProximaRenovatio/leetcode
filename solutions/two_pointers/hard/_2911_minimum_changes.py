
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float("inf")

        cost = [[INF] * (n + 1) for _ in range(n + 1)]

        # Precompute the minimum cost for every substring
        for i in range(n):
            for j in range(i + 1, n + 1):
                m = j - i

                for d in range(1, m):
                    if m % d != 0:
                        continue

                    changes = 0

                    for x in range(m // 2):
                        y = (m // d - 1 - x // d) * d + x % d

                        if s[i + x] != s[i + y]:
                            changes += 1

                    cost[i][j] = min(cost[i][j], changes)

        # DP: first i characters divided into j segments
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for i in range(2, n + 1):
            for j in range(1, min(k, i // 2) + 1):
                for h in range(2 * (j - 1), i - 1):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[h][j - 1] + cost[h][i]
                    )

        return dp[n][k]
