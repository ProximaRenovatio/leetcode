class Solution:
    def totalNumbers(self, digits: list[int]) -> int:
        nums = dict.fromkeys(range(10), 0)
        for i in digits:
            nums[i] += 1
        
        res = 0
        for i in range(100, 1000, 2):
            temp = nums.copy()
            found = True
            
            for j in range(3):
                d = int(str(i)[j])
                temp[d] -= 1
                if temp[d] < 0:
                    found = False
                    
            if found:
                res += 1
        return res