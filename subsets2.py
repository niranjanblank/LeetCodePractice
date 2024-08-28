"""
90. Subsets II
Medium
Topics
Companies
Given an integer array nums that may contain duplicates, return all possible
subsets
 (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        # Sort the list to ensure duplicates are adjacent
        nums.sort()

        def backtrack(i, subset):
            if i >= len(nums):
                # If we've considered all elements, add the current subset to the result
                result.append(subset.copy())
                return

            # Include the current number in the subset and move to the next element
            subset.append(nums[i])
            backtrack(i + 1, subset)

            # Exclude the current number from the subset
            subset.pop()

            # Skip over duplicate numbers to avoid creating duplicate subsets
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Move to the next distinct element
            backtrack(i + 1, subset)

        # Start the backtracking process with the first element and an empty subset
        backtrack(0, [])
        return result