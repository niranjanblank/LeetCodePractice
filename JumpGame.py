"""
55. Jump Game
Medium
Topics
Companies
You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.



Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""


def canJump(nums):
    # Initialize 'farthest' to 0, which keeps track of the farthest position we can reach
    farthest = 0

    # Iterate through each index 'i' of the array
    for i in range(len(nums)):
        # If the current index is greater than the farthest reachable index, return False
        # This means we're stuck and can't move forward to reach this index
        if i > farthest:
            return False

        # Update 'farthest' to be the maximum of the current 'farthest' and 'i + nums[i]'
        # 'i + nums[i]' calculates the furthest we can reach from the current index
        farthest = max(farthest, i + nums[i])

        # If 'farthest' reaches or exceeds the last index, return True indicating success
        if farthest >= len(nums) - 1:
            return True

    # If we exit the loop without having reached or exceeded the last index, return False
    return False

print(canJump([3,2,1,0,4]))