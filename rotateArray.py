"""
189. Rotate Array
Medium

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:

1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105


Follow up:

Try to come up with as many solutions as you can. There are at least three different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""

def rotate(nums, k):
    for i in range(k):
        temp = nums[-1]
        for j in range(len(nums)):
            nums[j], temp = temp, nums[j]
    return nums



def rotateBetter(nums, k):
    n = len(nums)
    k = k % n
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    # reverse the entire array
    reverse(0, n-1)
    print(nums)
    reverse(0,k-1)

    reverse(k, n-1)

    print(nums)

rotateBetter( nums = [1,2,3,4,5,6,7], k = 3)