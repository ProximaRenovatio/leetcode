class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        res = -1
        n = len(nums)
        
        for i in range(n-l+1):
            
            for j in range(min(n-i,r-l+1)):       
                s = sum(nums[i:i+l+j])
                if s > 0 and (res == -1 or s < res):
                    res = s
                    
        return res
                