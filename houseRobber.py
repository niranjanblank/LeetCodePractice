"""
198. House Robber
Medium
Topics
Companies
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 2:

Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 400
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialize two variables to keep track of the maximum profit
        # `rob1` represents the maximum profit up to the house before the previous one
        # `rob2` represents the maximum profit up to the previous house
        rob1, rob2 = 0, 0

        # Iterate through each house's value in the `nums` list
        for num in nums:
            # Calculate the maximum profit if we were to rob the current house
            # `temp` will store the maximum of either:
            # 1. The profit from robbing this house plus the profit from `rob1` (i.e., robbing up to the house before the last one),
            # or
            # 2. The profit from not robbing this house, keeping the current max profit (`rob2`)
            temp = max(rob1 + num, rob2)

            # Update `rob1` to be the value of `rob2` (shifting the window forward)
            rob1 = rob2
            # Update `rob2` to be the new max profit after considering the current house
            rob2 = temp

        return rob2