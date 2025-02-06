"""
1726. Tuple with Same Product
Medium
Topics
Companies
Hint
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

 

Example 1:

Input: nums = [2,3,4,6]
Output: 8
Explanation: There are 8 valid tuples:
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
Example 2:

Input: nums = [1,2,4,5,10]
Output: 16
Explanation: There are 16 valid tuples:
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 104
All elements in nums are distinct.
"""

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        # Time: O(n^2)
        # Space: O(n^2)
        # Dictionary to store the frequency of each unique product
        freq_count = defaultdict(int)

        # Iterate through all unique pairs (i, j) where i < j
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):  # Ensure unique pairs (avoid i == j)
                product = nums[i] * nums[j]
                freq_count[product] += 1  # Count occurrences of each product
        
        num_of_tuples = 0
        
        # Iterate through frequency dictionary to count valid tuples
        for product, freq in freq_count.items():
            if freq > 1:  # If there are at least two pairs with the same product
                # The number of ways to choose two pairs (a, b) and (c, d) with the same product
                # Formula: C(freq, 2) = freq * (freq - 1) // 2
                # Each valid selection contributes 8 different permutations

                # Why multiply by 8?
                # If we find two pairs (a, b) and (c, d) such that:
                # a * b = c * d, then we can form four ordered tuples:
                # (a, b, c, d), (a, b, d, c), (b, a, c, d), (b, a, d, c)
                # and also reverse the order of the second pair:
                # (c, d, a, b), (c, d, b, a), (d, c, a, b), (d, c, b, a)
                # This results in **8** valid permutations.

                num_of_tuples += 8 * (freq * (freq - 1)) // 2  # Integer division

        return num_of_tuples
