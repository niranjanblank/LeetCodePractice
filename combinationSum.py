"""
39. Combination Sum
Medium
Topics
Companies
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency
 of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []


Constraints:

1 <= candidates.length <= 30
2 <= candidates[i] <= 40
All elements of candidates are distinct.
1 <= target <= 40
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # to hold the results
        result = []

        # function for recursion
        # i points to the index starting which we can choose from candidates
        # curr holds the combination we have
        # total holds the sum of the combination
        def dfs(i, curr, total):
            # if the total is equal to the target, we add curr to the result
            if total == target:
                # we use shallow copy of curr as curr.copy() to store current combination to result
                # this will prevent future modification to curr from affecting the stored combination
                result.append(curr.copy())
                return

            # if we reach beyond the list of candidates or if the total surpasses the target, we ignore
            if total > target or i >= len(candidates):
                return

            # now we go path two paths,
            # path 1 add the current candidate to the curr list and all future paths will have this candidate
            # this will increase the total for the branch in which this candidate belong
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])

            # path 2 dont add the current candidate to the curr list
            # this will make the total as it is, and all future paths wont have this candidate
            curr.pop()
            dfs(i + 1, curr, total)

        # we start our dfs
        dfs(0, [], 0)
        return result