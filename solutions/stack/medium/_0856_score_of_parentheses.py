class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:

            if char == '(':
                # Start a new nested group
                stack.append(0)

            else:
                # Get the score inside the current parentheses
                inner_score = stack.pop()

                # "()" has score 1.
                # "(A)" has score 2 * A.
                score = max(2 * inner_score, 1)

                # Add the score to the parent level
                stack[-1] += score

        return stack[0]

