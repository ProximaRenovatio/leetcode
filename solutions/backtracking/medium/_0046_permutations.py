class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = [[[nums[0]]]] +  [[] for _ in range(n-1)]
        
        for level in range(1,n):
            for permut in res[level-1]:
                for i in range(level+1):                        
                    res[level].append(permut[0:i] + [nums[level]]+permut[i:level])
        return res[n-1]