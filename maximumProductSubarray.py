"""
152. Maximum Product Subarray
Medium
Topics
Companies
Given an integer array nums, find a
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.



Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # storing current max among all the numbers
        res = max(nums)

        cur_max, cur_min = 1, 1

        for n in nums:
            # if n is 0, we just ignore it by settin cur_max, cur_min to 1
            if n == 0:
                cur_max, cur_min = 1, 1
                continue

            temp = n * cur_max
            cur_max = max(temp, n * cur_min, n)
            cur_min = min(temp, n * cur_min, n)

            # set the max
            res = max(cur_max, res, cur_min)

        return res