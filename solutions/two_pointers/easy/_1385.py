class Solution:
        def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
                res = 0
                        
                                for num1 in arr1:
                                            valid = True
                                                        
                                                                    for num2 in arr2:
                                                                                    if abs(num1-num2) <= d:
                                                                                                        valid = False
                                                                                                                            
                                                                                                                                        if valid:
                                                                                                                                                        res+=1
                                                                                                                                                                        
                                                                                                                                                                                return res