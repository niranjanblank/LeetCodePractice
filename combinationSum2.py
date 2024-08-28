"""
90. Subsets II
Solved
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
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        # Sort the candidates to facilitate skipping duplicates
        candidates.sort()

        def dfs(i, curr_items, total):
            if total == target:
                # If the current total matches the target, add the combination to the result
                result.append(curr_items.copy())
                return

            # If the current total exceeds the target or we've exhausted the list, stop the search
            if total > target or i >= len(candidates):
                return

            # Include the current candidate in the combination and move to the next element
            curr_items.append(candidates[i])
            dfs(i + 1, curr_items, total + candidates[i])

            # Exclude the current candidate from the combination
            curr_items.pop()
            # Skip over duplicate candidates to avoid duplicate combinations
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            # Move to the next distinct candidate
            dfs(i + 1, curr_items, total)

        # Start the depth-first search with the first candidate, an empty combination, and a total of 0
        dfs(0, [], 0)

        return result