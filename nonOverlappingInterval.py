"""
435. Non-overlapping Intervals
Medium
Topics
Companies
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Constraints:

1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
"""

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sorting the intervals
        intervals.sort()
        # keep track of number of times interval is removed
        res = 0
        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            # checking for non overlap
            if start >= prev_end:
                # there is no overlap so just update the prev_end to new end
                prev_end = end
            else:
                # in case of overlap, we remove the one with max end value
                res += 1
                prev_end = min(prev_end, end)

        return res
