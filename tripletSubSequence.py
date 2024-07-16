"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.



Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.


Constraints:

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
"""


def increasingTriplet(nums):
    # Initialize two variables to store the smallest and second smallest elements seen so far.
    # We start them at infinity since we haven't seen any elements yet.
    first_min = float("inf")
    second_min = float("inf")

    # Iterate through each number in the list.
    for num in nums:
        # If the current number is less than or equal to the smallest number seen so far,
        # update the smallest number.
        if num <= first_min:
            first_min = num
        # If the current number is greater than the smallest number but less than or equal
        # to the second smallest, update the second smallest number.
        elif num <= second_min:
            second_min = num
        # If the current number is greater than both the smallest and second smallest numbers,
        # we have found an increasing triplet and return True.
        else:
            return True

    # If no increasing triplet is found in the entire list, return False.
    return False

print(increasingTriplet([2,1,5,0,4,6]))