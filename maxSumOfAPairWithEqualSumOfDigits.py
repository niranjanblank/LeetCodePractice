"""
2342. Max Sum of a Pair With Equal Sum of Digits
Solved
Medium
Topics
Companies
Hint
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
"""

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # Time Complexity: O(nlogn)
        # Space Complexity: O(n)
        hash_table = defaultdict(list)

        for num in nums:
            hash_table[self.sumOfDigits(num)].append(num)
      
        max_val = 0
        for key, val in hash_table.items():
            if len(val) > 1:
                 val.sort()
                 max_val = max(max_val, val[-1]+val[-2])

        return -1 if max_val == 0 else max_val
  

    
    def sumOfDigits(self, a):
        sum_a = 0
        while(a!=0):
            sum_a += a % 10
            a = a // 10
        return sum_a

class Solution2:
# Exceeds TLE
# Time Complexity: O(n^2 + nlogn)
# Space Complexity: O(n)
    def maximumSum(self, nums: List[int]) -> int:
        res = []

        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if self.sumOfDigits(nums[i]) == self.sumOfDigits(nums[j]):
                    res.append(nums[i]+nums[j])

        res.sort()

        return res[-1] if res else -1


    
    def sumOfDigits(self, a):
        sum_a = 0
        while(a!=0):
            sum_a += a % 10
            a = a // 10
        return sum_a

