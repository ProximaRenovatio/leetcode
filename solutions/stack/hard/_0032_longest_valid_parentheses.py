class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # Stack stores indices.
        # -1 acts as a base index before the string starts.
        stack = [-1]

        max_length = 0

        for i, char in enumerate(s):

            if char == '(':
                # Store the index of the opening parenthesis.
                stack.append(i)

            else:
                # Try to match this closing parenthesis
                # with the most recent opening parenthesis.
                stack.pop()

                if not stack:
                    # There is no opening parenthesis to match.
                    # This ')' becomes the new starting point.
                    stack.append(i)

                else:
                    # The current valid substring starts
                    # right after stack[-1].
                    current_length = i - stack[-1]

                    max_length = max(
                        max_length,
                        current_length
                    )

        return max_length