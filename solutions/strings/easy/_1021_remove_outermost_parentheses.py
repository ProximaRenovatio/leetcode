# With list

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        nested = 0

        for char in s:
            if char == "(":
                if nested > 0:
                    res.append(char)
                nested += 1

            else:
                if nested > 1:
                    res.append(char)
                nested -= 1
                
        return "".join(res)

"""
# With string

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = ""
        nested = 0

        for char in s:
            if char == "(":
                if nested > 0:
                    res += char
                nested += 1

            else:
                if nested > 1:
                      res += char
                nested -= 1
                
        return res

"""


"""
# With stack

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        res = []

        for char in s:
            if char == "(":
                if stack:
                    res.append(char)
                stack.append(char)

            else:
                stack.pop()
                if stack:
                    res.append(char)

        return "".join(res)
"""