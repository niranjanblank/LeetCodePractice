"""
416. Partition Equal Subset Sum
Medium
Topics
Companies
Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        # for the last element, the sum would be either 0 or that number,
        # so to initialize it we add 0
        dp.add(0)

        target = sum(nums) // 2

        for i in range(len(nums)-1,-1,-1):
            nextDP = set()

            for t in dp:
                nextDP.add(t + nums[i])
                nextDP.add(t)

            dp = nextDP

        return True if target in dp else False