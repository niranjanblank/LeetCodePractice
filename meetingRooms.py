"""
Description
Given an array of meeting time intervals consisting of start and end times [(s1,e1),(s2,e2),...] (si < ei), determine if a person could attend all meetings.


0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000


[(0,8), (8,10)] is not conflict at 8
Example
Example1

Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30), (5,10) and (0,30),(15,20) will conflict
Example2

Input: intervals = [(5,8),(9,15)]
Output: true
Explanation:
Two times will not conflict
"""

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        intervals.sort(key=lambda x: x.start)
        curr_interval = intervals[0]

        for interval in intervals[1:]:
            if interval.start < curr_interval.end:
                return False
            curr_interval = interval

        return True