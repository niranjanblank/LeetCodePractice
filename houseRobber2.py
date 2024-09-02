"""
213. House Robber II
Medium
Topics
Companies
Hint
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.



Example 1:

Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.
Example 2:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Example 3:

Input: nums = [1,2,3]
Output: 3


Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 1000
Seen this question in a real interview before?
1/5
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # since first is connected to last house, removing first in this case
        loot_1 = self.rob_helper(nums[1:])
        # since first is connected to last house, removing last in this case
        loot_2 = self.rob_helper(nums[0:-1])
        return max(loot_1, loot_2)

    def rob_helper(self, sub_array):
        rob1, rob2 = 0, 0

        for num in sub_array:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp

        return rob2
