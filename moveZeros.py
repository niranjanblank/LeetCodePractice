"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

"""


def move_zeroes(nums):
    # initializing the first position to place the non-zero item
    pos_to_place_non_zero_item = 0

    for i in range(len(nums)):
        # if we find non zero item, we place it in pos_to_place_non_zero_item, and increase the pos_to_place_non_zero_item
        if nums[i] != 0:
            nums[i], nums[pos_to_place_non_zero_item] = nums[pos_to_place_non_zero_item], nums[i]
            pos_to_place_non_zero_item += 1

    print(nums)
move_zeroes([ 1, 1,0,0, 3, 12])
