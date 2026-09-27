class Solution:
        def reverseParentheses(self, s):
                stack = []
                        current = []

                                for char in s:

                                            if char == '(':
                                                            # Save the current string before entering
                                                                            # a new pair of parentheses.
                                                                                            stack.append(current)

                                                                                                            # Start building the substring inside parentheses.
                                                                                                                            current = []

                                                                                                                                        elif char == ')':
                                                                                                                                                        # Reverse the substring inside the parentheses.
                                                                                                                                                                        current.reverse()

                                                                                                                                                                                        # Restore the string that was outside the parentheses.
                                                                                                                                                                                                        previous = stack.pop()

                                                                                                                                                                                                                        # Append the reversed substring to it.
                                                                                                                                                                                                                                        previous.extend(current)

                                                                                                                                                                                                                                                        current = previous

                                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                                                    # Normal character: add it to the current substring.
                                                                                                                                                                                                                                                                                                    current.append(char)

                                                                                                                                                                                                                                                                                                            return ''.join(current)