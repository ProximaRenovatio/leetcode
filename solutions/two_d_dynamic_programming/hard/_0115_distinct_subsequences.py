class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def check_substring(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == t[j]:
                memo[(i, j)] = check_substring(i + 1, j + 1) + check_substring(i + 1, j)
            else:
                memo[(i, j)] = check_substring(i + 1, j)

            return memo[(i, j)]

        return check_substring(0, 0)