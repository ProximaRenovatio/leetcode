class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        
        res = 1
        sign = 1
        
        if n < 0:
            n = - n
            x = 1/x
            
        if x < 0:
            x = -x
            if n % 2 !=0:
               sign = -1
        
        for i in range(n):
            res = res * x
            if res == 0 or abs(res) == 1:
                return res * sign
            
        return res * sign