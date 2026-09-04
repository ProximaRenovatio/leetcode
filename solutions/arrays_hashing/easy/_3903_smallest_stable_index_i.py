class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        max_l = [None] * n
        min_r = [None] * n

        for i in range(n):

            if i==0 or nums[i] > max_l[i-1]:
                max_l[i] = nums[i]
            else: 
                max_l[i] = max_l[i-1]

            if i==0 or nums[n-1-i] < min_r[n-i]:
                min_r[n-1-i] = nums[n-1-i]
            else: 
                min_r[n-1-i] = min_r[n-i]

        for i in range(n):
            if max_l[i] - min_r[i] <= k:
                return i

        return -1