"""
33. Search in Rotated Sorted Array
Medium
Topics
Companies
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1


Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:

        mid = (left + right) // 2

        # checking if we found the target
        if nums[mid] == target:
            return mid

        # if this condition is met, we are in the left sorted array
        if nums[mid] >= nums[left]:
            if nums[mid] > target >= nums[left]:
                right = mid - 1
            else:
                left = mid + 1
        # right section of array
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:

            mid = (left + right) // 2

            if target == nums[mid]:
                return mid

            # checking if the mid is in left sorted array or right array

            if nums[mid] >= nums[left]:
                # we are in the left section
                # now we search for target here
                if nums[left] <= target < nums[mid]:
                    # target is in the left
                    right = mid - 1
                else:
                    # target isnt in the left section, so we go to right section
                    left = mid + 1
            else:
                # we are in the right section
                # search for target in the right
                if nums[right] >= target > nums[mid]:
                    # target is still in the right
                    left = mid + 1
                else:
                    # target is in the left, so we go there
                    right = mid - 1

        return -1

print(search(nums = [4,5,6,7,0,1,2], target = 0))
print(search(nums = [4,5,6,7,0,1,2], target = 3))