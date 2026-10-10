class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        # Binary search for the minimum maximum difference we can achieve
        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2

            # Operations needed to reduce every difference to at most mid
            needed = sum(max(0, d - mid) for d in diffs)

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        # Reduce all differences above the optimal threshold
        limit = left
        remaining = k

        for i in range(len(diffs)):
            reduction = max(0, diffs[i] - limit)
            diffs[i] -= reduction
            remaining -= reduction

        # Use remaining operations to reduce differences equal to limit
        for i in range(len(diffs)):
            if remaining == 0:
                break
            if diffs[i] == limit and limit > 0:
                diffs[i] -= 1
                remaining -= 1

        return sum(d * d for d in diffs)
    


"""

    import heapq

class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        # Use a max-heap to reduce the largest difference first
        heap = [-d for d in diffs]
        heapq.heapify(heap)

        while k > 0:
            largest = -heapq.heappop(heap)

            if largest == 0:
                break

            largest -= 1
            heapq.heappush(heap, -largest)
            k -= 1

        return sum(d * d for d in [-x for x in heap])

"""