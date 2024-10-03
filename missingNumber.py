"""
268. Missing Number
Solved
Easy
Topics
Companies
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.



Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.


Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
"""


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # time complexity O(n^2)
        # space complexity O(1)
        for i in range(len(nums) + 1):
            if i not in nums:
                return i

class Solution2:
    def missingNumber(self, nums: List[int]) -> int:
        # time complexity O(n)
        # space complexity O(1)
        # this calculates the sum of n numbers
        expected_sum = len(nums)*(len(nums)+1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

class Solution3:
    def missingNumber(self, nums: List[int]) -> int:
        # time complexity O(n)
        # space complexity O(n)
        hashset = set(range(len(nums)+1))
        print(hashset)
        for num in nums:
            if num in hashset:
                hashset.remove(num)
        return hashset.pop()

class Solution4:
    # time complexity: O(n)
    # space complexity: O(1)
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        return res