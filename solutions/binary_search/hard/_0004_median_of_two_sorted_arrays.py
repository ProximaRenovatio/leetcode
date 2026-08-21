from patterns.quick_sort.quick_sort import quick_sort 

'''
# Approach 1: Concatenate + sort 

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_list = nums1 + nums2
        n = len(merged_list)
        quick_sort(merged_list , 0, n-1)

        if n % 2:
            return merged_list [n // 2]

        return (merged_list [n // 2 - 1] + merged_list [n // 2]) / 2
'''


# Approach 3: Binary search partition

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        # Binary search on the smaller array.
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)

        # Search range for the partition in nums1.
        left, right = 0, m

        # Number of elements that must be on the left side.
        half = (m + n + 1) // 2

        while left <= right:

            # Number of elements taken from nums1.
            i = (left + right) // 2

            # Remaining elements needed from nums2.
            j = half - i

            # Elements immediately around the partition.
            l1 = nums1[i - 1] if i else float("-inf")
            r1 = nums1[i] if i < m else float("inf")
            l2 = nums2[j - 1] if j else float("-inf")
            r2 = nums2[j] if j < n else float("inf")

            # Correct partition:
            # every element on the left <= every element on the right.
            if l1 <= r2 and l2 <= r1:

                # Odd total length.
                if (m + n) % 2:
                    return max(l1, l2)

                # Even total length.
                return (max(l1, l2) + min(r1, r2)) / 2

            # Too many elements taken from nums1.
            if l1 > r2:
                right = i - 1

            # Too few elements taken from nums1.
            else:
                left = i + 1

'''
If I don't have the correct partition, 
I try again by shifting it appropriately. 
The partition always remains the same size 
(a total of “half” values, but taken more from one list than the other). 

And it is only interesting in analyzing what happens to 
the partition below the median (i and j = half-i) because 
the median divides the interval exactly in half, the vectors are sorted, 
and automatically the correct lower partition will ensure that 
all values greater than the median end up in the upper partition.

The idea is that shifting the partition to half the size of 
the merge of the lists means searching for a new list 
containing all and only the values less than or equal to the median.
'''



'''Conclusion             
                
# Approach                  Time                Memory

1 Concatenate + sort        O(n log n)          O(n)
2 Two-pointer merge         O(n)                O(n)
3 Binary search partition   O(log(min(m,n))     O(1)        ← optimal     


Thanks by the combination of three properties:

1. The median divides the elements into two groups of nearly equal size.
2. The arrays are already sorted, so we can represent each group using a simple partition.
3. Once the partition in one array is fixed, the partition in the other is determined.

allows to go from:

        concatenate + sort               ->  O((m+n) log(m+n))

to:

        binary search on the partition   ->  O(log(min(m,n)))                   
                
'''