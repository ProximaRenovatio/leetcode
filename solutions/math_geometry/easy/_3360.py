class Solution:
        def canAliceWin(self, n: int) -> bool:
                s = 10
                        
                                while n >= 0 and s > 0:
                                            n -= s
                                                        s -= 1
                                                                
                                                                        return not s%2 
                                                                                    