from solutions.binary_search.hard._0004_median_of_two_sorted_arrays import Solution

def test_findMedianSortedArrays():
    solution = Solution()

    assert solution.findMedianSortedArrays([1, 3], [2]) == 2.00000
    assert solution.findMedianSortedArrays([1, 2], [3,4]) == 2.5000
    assert solution.findMedianSortedArrays([1, 12, 13], [2,3,4,5,6,7,8,9,10,11]) == 7


'''COMPLETE TRACE
┌──────────────────────────────────────────────┐
│ nums1 = [1, 12, 13]                          │
│ nums2 = [2,3,4,5,6,7,8,9,10,11]              │
└──────────────────────────────────────────────┘

total  = 13
half   = 7

SEARCH nums1
left = 0
right = 3

          i = 1
          j = 6

nums1: [1] | [12,13]
nums2: [2,3,4,5,6,7] | [8,9,10,11]

l1 = 1
r1 = 12
l2 = 7
r2 = 8

l1 <= r2  → 1 <= 8  ✅
l2 <= r1  → 7 <= 12 ✅

PARTITION FOUND

left side  = [1,2,3,4,5,6,7]
right side = [8,9,10,11,12,13]

median = max(1,7)
       = 7
'''




'''ALL POSSIBLE PARTITIONS

i = 0
A: | 1 12 13
B: [2 3 4 5 6 7 8] | [9 10 11]

i = 1
A: 1 | 12 13
B: [2 3 4 5 6 7] | [8 9 10 11]         -> correct l1 <= r2 and l2 <= r1

i = 2
A: 1 12 | 13
B: [2 3 4 5 6] | [7 8 9 10 11]

i = 3
A: 1 12 13 |
B: [2 3 4] | [5 6 7 8 9 10 11]

'''