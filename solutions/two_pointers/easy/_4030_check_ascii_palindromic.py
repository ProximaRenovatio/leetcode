class Solution:
    def isPalindromic(self, s: str) -> bool:
        bin = ""
        
        for i in range(len(s)):
            bin += (format(ord(s[i]),'08b'))

        n = len(bin)
        print(bin)
        is_palindrome = True
        for i in range(n // 2):
            if bin[i] != bin[n-i-1]:
                is_palindrome = False
                print(i,n-i)
        return is_palindrome