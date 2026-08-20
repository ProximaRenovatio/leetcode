class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = ""
        maxLength = 0

        for i, chr in enumerate(s): 
            if chr not in window:
                window += chr
                maxLength = max(maxLength, len(window))
            else:
                window = window[window.find(chr) + 1 :] + chr

        return maxLength