class Solution:
    def reverse(self, x: int) -> int:
        
        sign = 1        
        if x < 0:
            x = - x
            sign = -1
        res = x % 10
        
        while x // 10:
            x = x // 10
            
            if (res < pow(2,31) // 10) or (res == pow(2,31) // 10 and x % 10 < 8): 
                res = res * 10 + x % 10    
            else:
                return 0
                                
        return sign * res 