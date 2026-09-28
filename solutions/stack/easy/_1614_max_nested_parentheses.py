class Solution:
        def maxDepth(self, s: str) -> int:
                res = 0
                        cont = 0
                                
                                        for c in s:
                                                    if c == '(':
                                                                    cont += 1                
                                                                                    if cont > res:
                                                                                                        res = cont
                                                                                                                    elif c == ')':
                                                                                                                                    cont -= 1
                                                                                                                                                   
                                                                                                                                                           return res
                                                                                                                                                                           
                                                                                                                                                                                       