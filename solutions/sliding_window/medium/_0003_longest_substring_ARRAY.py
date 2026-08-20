class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = [-1] * 128
        left = 0
        max_length = 0

        for right, char in enumerate(s.encode()):
            previous = last_seen[char]

            if previous >= left:
                left = previous + 1

            last_seen[char] = right

            length = right - left + 1
            max_length = max(max_length, length)

        return max_length