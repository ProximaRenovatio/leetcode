class Solution:
        def checkString(self, s: str) -> bool:
                b_founded = False
                        res = True
                            
                                
                                        for c in s:
                                                    if c == 'b':
                                                                    b_founded = True
                                                                                elif b_founded:
                                                                                                res = False
                                                                                                            
                                                                                                                    return res