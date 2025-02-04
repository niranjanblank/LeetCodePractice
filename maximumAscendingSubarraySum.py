"""
1800. Maximum Ascending Subarray Sum
Solved
Easy
Topics
Companies
Hint
Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.

A subarray is defined as a contiguous sequence of numbers in an array.

A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

 

Example 1:

Input: nums = [10,20,30,5,10,50]
Output: 65
Explanation: [5,10,50] is the ascending subarray with the maximum sum of 65.
Example 2:

Input: nums = [10,20,30,40,50]
Output: 150
Explanation: [10,20,30,40,50] is the ascending subarray with the maximum sum of 150.
Example 3:

Input: nums = [12,17,15,13,10,11,12]
Output: 33
Explanation: [10,11,12] is the ascending subarray with the maximum sum of 33.
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
"""

class Solution1:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        l = 0
        max_sum = 0
        curr_sum = nums[l]
        for r in range(1,len(nums)):
            if nums[r-1] < nums[r]:
                curr_sum+=nums[r]
            else:
                max_sum = max(max_sum,curr_sum)
                l = r
                curr_sum = nums[l]

        return max(max_sum,curr_sum)

class Solution2:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # Time Complexity: O(n^2)
        # Space Complexity: O(1)

        l = 0
        curr_sum = nums[l]
        for r in range(1,len(nums)):
            if nums[r-1] < nums[r]:
                curr_sum = max(curr_sum, sum(nums[l:r+1]))
            else:
                l = r

        return curr_sum
