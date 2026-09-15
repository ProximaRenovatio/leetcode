class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] is True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        # Build the palindrome DP table.
        # We process shorter substrings before longer ones.
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or pal[i + 1][j - 1]):
                    pal[i][j] = True

        # dp[i] = maximum number of non-overlapping palindromes
        # that can be selected from s[0:i+1].
        dp = [0] * n

        for i in range(n):
            # Option 1: do not use a palindrome ending at i.
            dp[i] = dp[i - 1] if i > 0 else 0

            # Option 2: choose a palindrome s[j:i+1].
            for j in range(i + 1):
                length = i - j + 1

                if length >= k and pal[j][i]:
                    # If j == 0, there is no previous interval.
                    # Otherwise, we can use the best solution up to j-1.
                    previous = dp[j - 1] if j > 0 else 0

                    dp[i] = max(dp[i], previous + 1)

        return dp[n - 1]