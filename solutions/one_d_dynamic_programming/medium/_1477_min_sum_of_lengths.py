class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:

        n = len(arr)
        best = [float('inf')] * n

        # best[i] = minimum length of a valid subarray
        # that ends at or before index i
        total = 0
        left = 0
        answer = float('inf')

        for right in range(n):
            total += arr[right]

            # Remove elements from the left if the sum is too big
            while total > target:
                total -= arr[left]
                left += 1

            # We found a subarray with sum equal to target
            if total == target:
                length = right - left + 1

                # Check if there is another valid subarray before it
                if left > 0 and best[left - 1] != float('inf'):
                    answer = min(answer, length + best[left - 1])

                # Save the shortest valid subarray found so far
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)

            else:
                # Keep the previous best value
                if right > 0:
                    best[right] = best[right - 1]

        # No two non-overlapping subarrays were found
        if answer == float('inf'):
            return -1

        return answer