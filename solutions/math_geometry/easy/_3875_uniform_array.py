class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # the problem condition is always true, so immediately return true is enough
        # return true   

        n = len(nums1)
        nums2 = []
        odd_idx = [i for i in range(n) if not nums1[i] % 2 ]

        print (odd_idx)

        if not odd_idx or len(odd_idx) == len(nums1):
            nums2 = nums1
        else:
            nums2 = [nums1[i] if i in odd_idx else nums1[i]-nums1[odd_idx[0]] for i in range(n) ]

        print (nums2)
        
        return bool(nums2)

    