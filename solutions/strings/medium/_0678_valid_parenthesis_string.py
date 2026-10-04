class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0

        for char in s:

            if char == "(":
                low += 1
                high += 1

            elif char == ")":
                low -= 1
                high -= 1

            else:  # '*'
                # '*' can be either:
                # '(' -> balance + 1
                # ')' -> balance - 1
                # ''  -> balance unchanged

                low -= 1
                high += 1

            # We cannot have a negative balance.
            # If even the maximum possible balance is negative,
            # there is no way to make the string valid.
            if high < 0:
                return False

            # The minimum balance cannot be negative.
            # We can use '*' as an empty string or as '('
            # to keep the balance at 0.
            low = max(low, 0)

        # If balance 0 is possible, the string is valid.
        return low == 0