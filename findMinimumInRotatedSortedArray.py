"""
153. Find Minimum in Rotated Sorted Array
Medium
Topics
Companies
Hint
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.



Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.


Constraints:

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
All the integers of nums are unique.
nums is sorted and rotated between 1 and n times.
"""

def findMin(nums):
    # Initialize result with the first element of the array
    res = nums[0]

    # Set pointers for binary search
    left, right = 0, len(nums) - 1

    while left <= right:
        # Check if the current window is already sorted
        if nums[left] < nums[right]:
            # If sorted, the minimum element is the leftmost element
            res = min(res, nums[left])
            break

        # Calculate the middle index
        mid = (left + right) // 2
        # Update the result with the middle element
        res = min(res, nums[mid])

        # Determine if the left portion is sorted
        if nums[mid] >= nums[left]:
            # If true, the minimum must be in the right portion
            left = mid + 1
        else:
            # Otherwise, the minimum is in the left portion
            right = mid - 1

    return res

print(findMin(nums = [4,5,6,7,0,1,2]))
print(findMin(nums = [11,13,15,17]))