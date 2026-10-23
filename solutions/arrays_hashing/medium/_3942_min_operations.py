class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        counterSign = 1

        # Determine the circular direction
        if nums[1] == (nums[0] - 1) % n:
            counterSign = -1
        elif nums[1] != (nums[0] + 1) % n:
            return -1

        # Verify that the whole permutation follows that direction
        for i in range(2, n):
            if nums[i] != (nums[i - 1] + counterSign) % n:
                return -1

        # Find the minimum number of operations
        if counterSign == 1:
            return min((n - nums[0]) % n, nums[0] + 2)
        else:
            k = (n - 1 - nums[0]) % n
            return 1 + min(k, (n - k) % n)




"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        zero = nums.index(0)

        counterSign = 1

        for i in range(n):
            if nums[(zero + i) % n] != i:
                counterSign = 0
                break

        if counterSign == 1:
            return min(zero, n - zero + 2)

        counterSign = -1

        for i in range(n):
            if nums[(zero - i) % n] != i:
                counterSign = 0
                break

        if counterSign == -1:
            return min(zero + 2, n - zero)

        return -1    """