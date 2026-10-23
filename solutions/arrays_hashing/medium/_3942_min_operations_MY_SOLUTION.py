# 3942. Minimum Operations to Sort a Permutation

class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)
        counterSign = 1
        
        if n == 1:
            return 0
            
        if n == 2:
            return nums[0]   

        # Determine the circular direction
        if (nums[1] == nums[0] - 1) or (nums[1] == nums[0] + n - 1):
            counterSign = -1
        elif (nums[1] != nums[0] + 1) and (nums[1] != nums[0] + 1 - n):
            return - 1

        # Verify that the whole permutation follows that direction  
        for i in range(2, n):
            if (nums[i] != nums[i - 1] + counterSign) and \
               (nums[i] != nums[i - 1] + counterSign - counterSign * n):
                return -1

        # Find the minimum number of operations       
        if counterSign == 1:
            return min((n - nums[0]) % n, nums[0] + 2)
        else:
            k = (n - 1 - nums[0]) % n
            return 1 + min(k, (n - k) % n)