"""
3151. Special Array I
Solved
Easy
Topics
Companies
Hint
An array is considered special if every pair of its adjacent elements contains two numbers with different parity.

You are given an array of integers nums. Return true if nums is a special array, otherwise, return false.

 

Example 1:

Input: nums = [1]

Output: true

Explanation:

There is only one element. So the answer is true.

Example 2:

Input: nums = [2,1,4]

Output: true

Explanation:

There is only two pairs: (2,1) and (1,4), and both of them contain numbers with different parity. So the answer is true.

Example 3:

Input: nums = [4,3,1,6]

Output: false

Explanation:

nums[1] and nums[2] are both odd. So the answer is false.
"""

class Solution:
    #Time Complexity: O(n)
    #Space Complexity : O(1)
    def isEven(self,x):
        return x%2==0
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True

        prev = self.isEven(nums[0])
        for i in  range(1,len(nums)):
            if prev == self.isEven(nums[i]):
                return False
            prev = self.isEven(nums[i])

        return True
        
