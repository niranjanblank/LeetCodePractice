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

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0 , len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                # we are in left sorted array
                if nums[left] <= target < nums[mid]:
                    # target is in left sorted array so we move right pointer
                    right = mid - 1
                else:
                    # we reach here if target is less than nums[left], neaning we have to go
                    # in the right sorted array, so we move left pointer
                    # of ig the target isnt in the left sorted array, we have to go to
                    # the right sorted array
                    left = mid + 1
            else:
                # we are in right sorted array
                if  nums[mid] < target <= nums[right]:
                    # target is in right sorted array so we move left pointer
                    left = mid + 1
                else:
                    # we reach here if target is greater than right, meaning we have to go
                    # in the left sorted array so we move the right pointer
                    # or if the target isnt in the right sorted array, we have to go to
                    # the left sorted array
                    right = mid -1
        return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right = 0 , len(nums)-1
        
        # finding the pivot elemtnt
        while left <= right:
            m = (left+right)//2
            if nums[m] > nums[-1]:
                left = m + 1
            else:
                right = m - 1

        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        # binary search on left side
        answer = binarySearch(0,left-1,target)

        if answer  != -1:
            return answer
        
        return binarySearch(left, len(nums)-1, target)

print(search(nums = [4,5,6,7,0,1,2], target = 0))
print(search(nums = [4,5,6,7,0,1,2], target = 3))
