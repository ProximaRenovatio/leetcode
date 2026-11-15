
class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
            MOD = 10**9 + 7

                    even = 1  # Number of even prefix sums
                            odd = 0   # Number of odd prefix sums
                                    parity = 0
                                            res = 0

                                                    for num in arr:
                                                                parity = (parity + num) % 2

                                                                            if parity == 1:
                                                                                            res += even
                                                                                                            odd += 1
                                                                                                                        else:
                                                                                                                                        res += odd
                                                                                                                                                        even += 1

                                                                                                                                                                    res %= MOD

                                                                                                                                                                            return res
                                                                                                                                                                            