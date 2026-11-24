
from math import gcd, lcm

class Solution:
    def maxLength(self, nums: list[int]) -> int:
            res = 0

                    for i in range(len(nums)):
                                prod = 1
                                            g = 0
                                                        l = 1

                                                                    for j in range(i, len(nums)):
                                                                                    x = nums[j]

                                                                                                    prod *= x
                                                                                                                    g = gcd(g, x)
                                                                                                                                    l = lcm(l, x)

                                                                                                                                                    if prod == g * l:
                                                                                                                                                                        res = max(res, j - i + 1)

                                                                                                                                                                                return res
                                                                                                                                                                                