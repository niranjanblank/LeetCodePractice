"""

"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # Sort all the start times of the intervals
        start = sorted([i.start for i in intervals])
        # Sort all the end times of the intervals
        end = sorted([i.end for i in intervals])

        # To store the maximum number of rooms required at any given time
        res = 0
        # To keep track of the current number of rooms in use
        count = 0

        # Pointers to iterate through start and end times
        start_pointer, end_pointer = 0, 0

        # Iterate through all the start times
        while start_pointer < len(intervals):
            # If the next meeting starts before the earliest ending meeting finishes,
            # we need an additional room.
            if start[start_pointer] < end[end_pointer]:
                count += 1
                start_pointer += 1
            else:
                # If the earliest ending meeting finishes before or at the same time
                # as the next meeting starts, we can free up a room.
                count -= 1
                end_pointer += 1

            # Update the result with the maximum number of rooms in use
            res = max(res, count)

        return res