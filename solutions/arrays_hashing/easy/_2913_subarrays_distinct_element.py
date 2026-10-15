class Solution:
    def sumCounts(self, nums: list[int]) -> int:
     n = len(nums)
     res = n
            
     for i in range(1, n):
         for j in range(n-i): 
             distinct = len(set(nums[j:j+i+1]))
             res += distinct * distinct
             
     return res