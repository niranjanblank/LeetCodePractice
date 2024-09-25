"""
300. Longest Increasing Subsequence
Medium
Topics
Companies
Given an integer array nums, return the length of the longest strictly increasing
subsequence
.



Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1


Constraints:

1 <= nums.length <= 2500
-104 <= nums[i] <= 104


Follow up: Can you come up with an algorithm that runs in O(n log(n)) time complexity?
"""


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # O(n2) solution
        #creating a cache to store length of subsequence from a point in the array
        # initially all will be 1, will be updated as we go from back to front
        LIS = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            # we we traverse from ith position till the end of nums
            for j in range(i+1, len(nums)):
                # if the num at i is less than num at j, then only we can expect an increasing subsequence
                if nums[i] < nums[j]:
                    # if the condition is true, there will be a increase in subsequence
                    LIS[i] = max(LIS[i], 1+LIS[j])

        return max(LIS)