class Solution:
        def resultArray(self, nums, k):
                # res[r] = total number of subarrays whose product % k == r
                        res = [0] * k

                                # dp[r] = number of subarrays ending at the current position
                                        # whose product % k == r
                                                dp = [0] * k

                                                        for num in nums:
                                                                    mod = num % k

                                                                                # DP for subarrays ending at the current number
                                                                                            new_dp = [0] * k

                                                                                                        # Start a new subarray containing only num
                                                                                                                    new_dp[mod] += 1

                                                                                                                                # Extend all previous subarrays by adding num
                                                                                                                                            for r in range(k):
                                                                                                                                                            new_remainder = (r * mod) % k
                                                                                                                                                                            new_dp[new_remainder] += dp[r]

                                                                                                                                                                                        # Add the current subarrays to the global result
                                                                                                                                                                                                    for r in range(k):
                                                                                                                                                                                                                    res[r] += new_dp[r]

                                                                                                                                                                                                                                # Move to the next position
                                                                                                                                                                                                                                            dp = new_dp

                                                                                                                                                                                                                                                    return res