class Solution:
        def smallestIndex(self, nums: List[int]) -> int:
                
                        for i,n in enumerate(nums):           
                                    tot = n % 10
                                                
                                                            while n // 10:
                                                                            n //= 10
                                                                                            tot += n % 10
                                                                                                                     
                                                                                                                                 if tot == i:
                                                                                                                                                 return i
                                                                                                                                                         
                                                                                                                                                                 return -1
                                                                                                                                                                                 