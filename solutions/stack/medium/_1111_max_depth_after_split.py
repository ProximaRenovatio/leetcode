class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        depth = 0

        for char in seq:

            if char == '(':
                # Increase the current nesting depth
                depth += 1

                # Alternate between the two groups
                res.append(depth % 2)

            else:
                # For a closing parenthesis, use the current depth
                # before decreasing it.
                res.append(depth % 2)

                # Decrease the nesting depth
                depth -= 1

        return res
        