"""
209. Minimum Size Subarray Sum
Solved
Medium
Topics
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
 

Constraints:

1 <= target <= 109
1 <= nums.length <= 105
1 <= nums[i] <= 104
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Time Complexity : O(n)
        # Space Complexity : O(1)

        left = 0
        curr_sum = 0
        
        ans = float('inf')

        for right in range(0,len(nums)):

            curr_sum += nums[right]

            while curr_sum >= target:
                ans = min(ans,right-left + 1)
                curr_sum-= nums[left]
                left+=1

        
        return ans if ans != float('inf') else 0
