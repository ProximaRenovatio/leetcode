class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        longest_pal = s[0]

        for i in range(1,n):
            even_pal = odd_pal = s[i]

            j = 0  #abcdcba  cbabdaaab
            wipO = wipE = True
            while j < min(n-i,i): 

                if wipO and i+j+1<n and s[i-j-1]==s[i+j+1]:
                    odd_pal = s[i-j-1] + odd_pal + s[i+j+1]
                else: wipO = False

                if wipE and s[i-j-1]==s[i+j]:
                    even_pal = s[i-j-1] + even_pal + s[i+j] if j>0 else s[i-1] + even_pal
                else: wipE = False

                print(even_pal, odd_pal)
                if not wipO and not wipE: 
                    break
                j+=1

            m = max(len(even_pal),len(odd_pal))
            if m > len(longest_pal):
                longest_pal = even_pal if len(even_pal) == m else odd_pal

        return longest_pal
