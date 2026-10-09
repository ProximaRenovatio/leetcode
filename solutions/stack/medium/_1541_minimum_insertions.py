# using list stack
class Solution:
    def minInsertions(self, s: str) -> int:
        res = 0
        stack = []
        balanced = True
        
        for c in s:
            if c == "(":                
                stack.append("(")
                if not balanced:
                    res += 1
                    balanced = True
            else:        
                if balanced:
                    balanced = False
                    if stack:
                        stack.pop()
                    else: 
                        res += 1  
                else:
                    balanced = True

        if not balanced:
            res += 1
        
        res += len(stack) * 2

        return res
    

""" # using numeric stack

class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_count = 0

        i = 0
        while i < len(s):
            if s[i] == '(':
                open_count += 1
            else:
                # Check whether the current ')' has a matching second ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    # Insert the missing second ')'
                    insertions += 1

                if open_count > 0:
                    open_count -= 1
                else:
                    # Insert a missing '('
                    insertions += 1

            i += 1

        # Every remaining '(' needs two closing parentheses
        insertions += open_count * 2

        return insertions
"""