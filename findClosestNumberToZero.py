"""
2239. Find Closest Number to Zero
Solved
Easy
Topics
Companies
Hint
Given an integer array nums of size n, return the number with the value closest to 0 in nums. If there are multiple answers, return the number with the largest value.



Example 1:

Input: nums = [-4,-2,1,4,8]
Output: 1
Explanation:
The distance from -4 to 0 is |-4| = 4.
The distance from -2 to 0 is |-2| = 2.
The distance from 1 to 0 is |1| = 1.
The distance from 4 to 0 is |4| = 4.
The distance from 8 to 0 is |8| = 8.
Thus, the closest number to 0 in the array is 1.
Example 2:

Input: nums = [2,-1,1]
Output: 1
Explanation: 1 and -1 are both the closest numbers to 0, so 1 being larger is returned.


Constraints:

1 <= n <= 1000
-105 <= nums[i] <= 105

"""


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # Initialize 'closest' to the first number in the list
        closest = nums[0]

        # Iterate over each number 'n' in the list 'nums'
        for n in nums:
            # Check if the absolute value of 'n' is smaller than the absolute value of 'closest'
            if abs(n) < abs(closest):
                closest = n  # Update 'closest' if 'n' is closer to zero

        # After the loop, check if the absolute value of 'closest' exists in the list
        # This ensures that we return the positive number if there is a tie between positive and negative numbers
        if abs(closest) in nums:
            return abs(closest)

        # Return 'closest' which might be either negative or positive if no positive equivalent exists
        return closest