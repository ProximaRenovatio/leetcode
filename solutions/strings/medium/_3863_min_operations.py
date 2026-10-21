
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Check whether the string is already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # A reversed string of length 2 cannot be sorted
        # because the entire string cannot be selected
        if n == 2:
            return -1

        mn = min(s)
        mx = max(s)

        # One operation is enough if one endpoint is already correct
        if s[0] == mn or s[-1] == mx:
            return 1

        # If the minimum or maximum is in the middle, two operations suffice
        if any(c == mn or c == mx for c in s[1:-1]):
            return 2

        # The minimum is at the end and the maximum is at the beginning
        return 3