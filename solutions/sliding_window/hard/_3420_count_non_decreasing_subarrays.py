from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dq = deque()

        cost = 0
        ans = 0
        right = n - 1

        for left in range(n - 1, -1, -1):
            num = nums[left]

            # Merge segments whose values are smaller than num
            while dq and nums[dq[-1]] < num:
                idx = dq.pop()
                next_idx = dq[-1] if dq else right + 1

                cost += (next_idx - idx) * (num - nums[idx])

            dq.append(left)

            # Shrink the window from the right
            while cost > k:
                cost -= nums[dq[0]] - nums[right]

                if dq[0] == right:
                    dq.popleft()

                right -= 1

            # Count valid subarrays ending within the window
            ans += right - left + 1

        return ans
