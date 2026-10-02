class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []

        def backtrack(current, open_count, close_count):
            # If we used all n pairs, we found a valid combination
            if len(current) == 2 * n:
                result.append(current)
                return

            # We can add '(' as long as we have not used all n
            # opening parentheses.
            if open_count < n:
                backtrack(
                    current + "(",
                    open_count + 1,
                    close_count
                )

            # We can add ')' only if there are unmatched
            # opening parentheses.
            if close_count < open_count:
                backtrack(
                    current + ")",
                    open_count,
                    close_count + 1
                )

        backtrack("", 0, 0)

        return result
