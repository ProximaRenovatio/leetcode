class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def digit_sum(n: int) -> int:
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        n = len(nums)

        # Sort by digit sum, then by numeric value
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each value to its target position
        target_index = {value: i for i, value in enumerate(sorted_nums)}

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or target_index[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = target_index[nums[j]]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps