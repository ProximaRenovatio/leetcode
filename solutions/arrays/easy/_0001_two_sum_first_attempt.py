"""
LeetCode 1 - Two Sum

Difficulty: Easy
Topics: Array, Hash Table
Pattern: Hash Map, Two-pass approach

First approach
--------------
I first created a dictionary containing all numbers and then
tracked the complementaries found during the traversal.

This solution works in O(n), but it requires more state and
multiple conditions.

Improved approach
-----------------
Store each number together with its index while traversing.

For each number:
    complement = target - num

If the complement has already been seen, return both indices.

Complexity:
Time: O(n)
Space: O(n)
"""



class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        myDict = dict.fromkeys(nums, 0)
        result = []
        complementsDetected = []

        for i, num in enumerate(nums):
            complement = target - num
 
            # if in the previous cycle the first index has been found, in the next cycles try to find the second index.
            if len(result)==1 and num == complementsDetected[1]:
                result.append(i)  

            # if 2 complementaries are present in the dictionary for the first time, save the first index.
            if (not result and complement in myDict) or (result and num!=complement and complementsDetected[0]==complementsDetected[1]):
                result = []
                result.append(i) 
                complementsDetected = [num, complement] 
                         
            
        return result
