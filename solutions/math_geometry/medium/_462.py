class Solution:
        def minMoves2(self, nums: list[int]) -> int:
                mean = 0
                        res = 0
                                mean = round(sum(nums) / len(nums))
                                        nearest = nums[0]
                                                minDist = float('inf')
                                                        
                                                                sort = sorted(nums)
                                                                        n = len(sort)
                                                                                mid = n // 2

                                                                                        if n % 2 == 1:
                                                                                                    median = sort[mid]
                                                                                                            else:
                                                                                                                        low = sort[mid-1]
                                                                                                                                    high = sort[mid]
                                                                                                                                                if abs(low-mean)<abs(high-mean):
                                                                                                                                                                median = low
                                                                                                                                                                            else:
                                                                                                                                                                                            median = high
                                                                                                                                                                                                        
                                                                                                                                                                                                                for num in nums:
                                                                                                                                                                                                                            res += abs(num-median)
                                                                                                                                                                                                                                        
                                                                                                                                                                                                                                                return res
                                                                                                                                                                                                                                                        