"""
15. 3Sum
Medium
Topics
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""


def threeSum(nums):
    # Sort the input list to make it easier to avoid duplicates and use two-pointer technique
    nums = sorted(nums)
    # Initialize an empty list to store the triplets
    answers = []

    # Iterate over the list with the index and the current number
    for i, curr_num in enumerate(nums):
        # Skip the same elements to avoid duplicate triplets
        if i > 0 and curr_num == nums[i - 1]:
            continue

        # Initialize two pointers
        left = i + 1
        right = len(nums) - 1

        # Use the two-pointer technique to find the triplets
        while left < right:
            total = curr_num + nums[left] + nums[right]

            # If the sum is greater than zero, move the right pointer to the left
            if total > 0:
                right -= 1
            # If the sum is less than zero, move the left pointer to the right
            elif total < 0:
                left += 1
            # If the sum is zero, add the triplet to the answers list
            else:
                answers.append([curr_num, nums[left], nums[right]])
                # Move the left pointer to the right
                left += 1
                # Skip the same elements to avoid duplicate triplets
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

    return answers
print(threeSum(nums = [-1,0,1,2,-1,-4]))
