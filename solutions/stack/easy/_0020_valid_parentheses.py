class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            
            if c in "{[(":
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    last_c = stack.pop()
                    if not (ord(c) + ord(last_c) in [81, 184, 248]):
                        return False
        return len(stack) == 0
                        
                    
