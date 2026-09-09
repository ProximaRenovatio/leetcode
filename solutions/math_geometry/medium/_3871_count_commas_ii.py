class Solution:
    def countCommas(self, n: int) -> int:    
       if n < 1000:
           return 0
       k = 0
       m = n
          
       while m // 1000:   
           m //= 1000
           k += 1
       
       res = ( n - 10**(k*3) + 1) * k    
       
       for i in range(1, k):
          res += (10**((i+1) * 3) - 10**(i*3)) * i
          
       return res    