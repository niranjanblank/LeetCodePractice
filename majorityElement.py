"""
169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2


Constraints:

n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109


Follow-up: Could you solve the problem in linear time and in O(1) space?
"""

def majorityElement(nums):
    nums_dict = {}

    for item in nums:
        nums_dict[item] = nums_dict.get(item,0)+1

    for key, value in nums_dict.items():
        if value > len(nums)/2:
            return key

def majorityElementBetter(nums):
    # boyer mayer method
    """
    This algorithm is efficient because it does not require additional space for counting occurrences.
    It leverages the fact that the majority element occurs more than n/2 times, so it can "cancel out"
    all other elements and still remain at the end.

    """
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count+= 1 if candidate==num else -1
    return candidate

print(majorityElementBetter([2,2,1,1,1,2,2]))