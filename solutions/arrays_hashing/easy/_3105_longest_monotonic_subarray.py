class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        
        previous = nums[0]
        inc = 1
        dec = 1
        max_inc = 1
        max_dec = 1
        
        for num in nums[1:]:
            if num > previous:
                inc += 1
                dec = 1
                max_inc = max(max_inc, inc)
            elif num < previous:
                inc = 1
                dec += 1
                max_dec = max(max_dec, dec)
            else:
                inc = 1
                dec = 1
                
            previous = num
                
        return max(max_inc, max_dec)