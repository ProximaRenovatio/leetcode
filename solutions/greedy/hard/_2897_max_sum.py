class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        res = 0
        counter = [0] * 30

        for num in nums:
            i = 0
            while num > 0:
                counter[i] += num & 1
                num >>= 1
                i += 1            
      
        for _ in range(k):
            i = 0
            best = 0
            cap = next((len(counter) - 1 - i for i, x in enumerate(reversed(counter)) if x != 0), -1)          
            for i in range(cap, -1, -1):
                if counter[i]>0:
                    best = best * 2 + 1
                    counter[i] -= 1
                else:
                    best = best * 2

            res += (best * best) % (10 ** 9 + 7)

        return res % (10 ** 9 + 7)