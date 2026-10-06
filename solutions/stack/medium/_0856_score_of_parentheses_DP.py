class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        level = 0

        for i in range(len(s)):

            if s[i] == '(':
                level += 1

            else:
                # We found "()"
                if s[i - 1] == '(':
                    dp[level] = 1

                # We found "(A)"
                else:
                    dp[level] *= 2

                # Add the current score to the parent level
                dp[level - 1] += dp[level]

                # Clear the current level
                dp[level] = 0

                # Go back to the parent level
                level -= 1

        return dp[0]


