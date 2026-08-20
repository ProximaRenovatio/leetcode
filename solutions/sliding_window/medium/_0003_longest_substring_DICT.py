class Solution:
    def lengthOfLongestSubstring(self,  s: str) -> int:
        subS = {}
        left = res = 0

        for right, char in enumerate(s):   
            if char in subS:
                left = max(left, subS[char] + 1)

            subS[char] = right
            res = max(res, right - left + 1)

        return res