class Solution:
        def minOperations(self, nums, x):
                total = sum(nums)
                        target = total - x

                                # We need to find the longest subarray
                                        # whose sum is equal to target.
                                                if target < 0:
                                                            return -1

                                                                    left = 0
                                                                            current_sum = 0
                                                                                    max_length = -1

                                                                                            for right in range(len(nums)):
                                                                                                        current_sum += nums[right]

                                                                                                                    # Shrink the window while its sum is too large
                                                                                                                                while left <= right and current_sum > target:
                                                                                                                                                current_sum -= nums[left]
                                                                                                                                                                left += 1

                                                                                                                                                                            # We found a valid subarray
                                                                                                                                                                                        if current_sum == target:
                                                                                                                                                                                                        max_length = max(
                                                                                                                                                                                                                            max_length,
                                                                                                                                                                                                                                                right - left + 1
                                                                                                                                                                                                                                                                )

                                                                                                                                                                                                                                                                        # No valid subarray was found
                                                                                                                                                                                                                                                                                if max_length == -1:
                                                                                                                                                                                                                                                                                            return -1

                                                                                                                                                                                                                                                                                                    # Everything outside the subarray must be removed
                                                                                                                                                                                                                                                                                                            return len(nums) - max_length