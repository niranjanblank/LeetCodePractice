"""
238. Product of Array Except Self
Solved
Medium
Topics
Companies
Hint
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.



Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

"""
# method 1
def productExceptSelf(nums):
    prefix = nums.copy()
    suffix = nums[::-1].copy()
    # fill the prefix and suffix
    for i in range(1,len(prefix)):
        prefix[i] = prefix[i]*prefix[i-1]
        suffix[i] = suffix[i]*suffix[i-1]
    suffix = suffix[::-1]
    nums[0] = suffix[1]
    nums[-1] = prefix[-2]

    for i in range(1, len(nums)-1):
        nums[i] = prefix[i-1]*suffix[i+1]
    return nums

# method 2

def productExceptSelf2(nums):
    result = [1]*len(nums)

    # calculate prefix product
    prefix_product = 1
    for i in range(len(nums)):
        result[i] *= prefix_product
        prefix_product *= nums[i]

    # suffix product
    suffix_product = 1
    for i in range(len(nums)-1,-1,-1):
        result[i] *= suffix_product
        suffix_product *= nums[i]
    return result

print(productExceptSelf2([1,2,3,4]))
