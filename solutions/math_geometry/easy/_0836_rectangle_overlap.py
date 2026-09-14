class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool: 
        
        if (rec1 == rec2):
            return True

        def check(a: list[int], b: list[int]):
           
           a = a + [a[0], a[3], a[2], a[1], a[0], (a[1]+a[3])/2, a[2], (a[1]+a[3])/2, (a[0]+a[2])/2, a[1], (a[0]+a[2])/2, a[3]]
           
           for i in range(8):
               cond =[ 
               a[i*2]  > b[0], 
               a[i*2+1]> b[1],
               a[i*2]  > b[0],
               a[i*2+1]< b[3],
               a[i*2]  < b[2],
               a[i*2+1]> b[1],
               a[i*2]  < b[2],
               a[i*2+1]< b[3] ]          
               
               if all(cond):
                  return True
           
           return False
              
        return check(rec1, rec2) or check(rec2, rec1)
        