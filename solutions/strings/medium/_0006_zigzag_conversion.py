''' # Solution using lists 

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # immediate escape
        if numRows == 1 or numRows >= len(s):
            return s

        # matrix with the final position of the characters
        rows = [[] for _ in range(numRows)]               
        inc = 1  
        j = 0  

        for i in range(len(s)):
            # append the next character in the correct row
            rows[j].append(s[i])

            # counter goes up and down through the rows
            if numRows > 1:
                if j == 0: 
                    inc = 1
                elif j == numRows-1:
                    inc = -1

                j = j + inc 

        # build the final string joining all the characters in the sorted matrix
        return ''.join(rows[i][j] for i in range(numRows) for j in range(len(rows[i])))
'''

# solution using strings      
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # immediate escape
        if numRows == 1 or numRows >= len(s):
            return s

        # matrix with the final position of the characters
        rows = ["" for _ in range(numRows)]               
        inc = 1  
        j = 0  

        for i in range(len(s)):
            # append the next character in the correct row
            rows[j]+=s[i]

            # counter goes up and down through the rows
            if j == 0: 
                inc = 1
            elif j == numRows-1:
                inc = -1

            j = j + inc 

        # build the final string joining all the characters in the sorted matrix
        return ''.join(rows)