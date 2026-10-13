class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        n = len(nums)
        res = 0

        nums.sort(key=abs)
        for i, num in enumerate(nums):
            if i < n // 2:
                res -= num * num
            else:
                res += num * num

        return res 