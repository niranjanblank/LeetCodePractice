"""
136. Single Number
Easy
Topics
Companies
Hint
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.



Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        # since 1 xor 1 = 0 , and 0 xor 0 = 0, if we are have duplicate numbers, they will be converted to 0
        # e.g 4= 100, so if we have two 4s then 100 xor 100 = 000
        # doing this in the end only number that doesnt have duplicate remain
        for n in nums:
            # ^ is bitwise xor operator
            res = res ^ n

        return res