"""
45. Jump Game II
Medium
Topics
Companies
You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2


Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 1000
It's guaranteed that you can reach nums[n - 1].
"""

def jump(nums):
    # Initialize the farthest reach and the end of the current jump range
    current_end = 0
    farthest = 0
    # Initialize the jump counter
    jumps = 0

    # Loop through the array up to the second last element
    for i in range(len(nums) - 1):
        # Update the farthest point reachable from the current indexasdasdsdmm
        farthest = max(farthest, i + nums[i])

        # If the current index is the end of the range of the current jump
        if i == current_end:
            # Increment the jump counter as we need another jump to extend our reach
            # to the furthest point identified within the current jump's range
            jumps += 1
            # Update the current end to the farthest point we can reach
            current_end = farthest

            # If the farthest point is beyond or at the last index, we don't need more jumps
            if farthest >= len(nums) - 1:
                return jumps

    # Return the total number of jumps needed to reach the last index
    return jumps

print(jump([2,3,0,1,4]))