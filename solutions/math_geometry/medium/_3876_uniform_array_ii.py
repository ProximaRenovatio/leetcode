class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        m = nums1[0]
        is_odd = is_even = False

        for num in nums1:
            if num < m:
                m = num
            if num % 2:
                is_odd = True
            else: 
                is_even = True

        if not is_odd or not is_even:
            return True
        
        if m % 2:
            return True
        else:
            return False