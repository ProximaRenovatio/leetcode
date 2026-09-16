class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n + 1)]
        sums = [[0] * (k + 1) for _ in range(n + 1)]

        # There is exactly one way to choose 0 segments: choose nothing
        for i in range(n + 1):
            dp[i][0] = 1
            sums[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, k + 1):

                # Case 1: do not use point i
                dp[i][j] = dp[i - 1][j]

                # Case 2: end a new segment at point i
                dp[i][j] += sums[i - 1][j - 1]

                dp[i][j] %= MOD

                # Keep a cumulative sum of previous DP states
                sums[i][j] = sums[i - 1][j] + dp[i][j]
                sums[i][j] %= MOD

        return dp[n][k]