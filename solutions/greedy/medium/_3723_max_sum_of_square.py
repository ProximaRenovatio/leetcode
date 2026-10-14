class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str: 
        if sum > 9 * num:
            return ""

        digits = []

        for _ in range(num):
            digit = min(9, sum)
            digits.append(str(digit))
            sum -= digit

        return ''.join(digits)

"""  Time exceed!! 
# Imposta il limite massimo a 110.000 cifre (abbastanza per le tue 100.000)
res = 0 
       
import sys
sys.set_int_max_str_digits(1000000)
        
        for i in range(num):
          res *= 10
          if sum > 9:
              sum -= 9
              res += 9
          elif sum > 0:
              res += sum
              sum = 0
          
        return str(res)
            
         """
            