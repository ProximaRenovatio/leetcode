class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]

        for char in s:class Solution:
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



    '''
    
    class Solution: def scoreOfParentheses(self, s: str) -> int: dp = [0] * (len(s) // 2 + 1) level = 0 i = 0 while i < len(s): if s[i] == '(': level =+ 1 else: dp[level] += 1 level -= 1 while i < len(s)-1 and s[i+1] == ")": dp[level] = dp[level+1] * 2 dp[level+1] = 0 level -= 1 i = i+1 i += 1 return dp[1] # ((())(())((())))
    
    
    
    
    
    
    '''
