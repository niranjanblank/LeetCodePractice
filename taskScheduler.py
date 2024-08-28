"""
621. Task Scheduler
Medium
Topics
Companies
Hint
You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint: identical tasks must be separated by at least n intervals due to cooling time.

​Return the minimum number of intervals required to complete all tasks.



Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2

Output: 8

Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have passed.

Example 2:

Input: tasks = ["A","C","A","B","D","B"], n = 1

Output: 6

Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.

With a cooling interval of 1, you can repeat a task after just one other task.

Example 3:

Input: tasks = ["A","A","A", "B","B","B"], n = 3

Output: 10

Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling twice between repetitions of these tasks.



Constraints:

1 <= tasks.length <= 104
tasks[i] is an uppercase English letter.
0 <= n <= 100
"""
import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Calculate the frequency of each task
        task_counts = Counter(tasks)

        # Create a max_heap so that we process tasks with higher frequency first
        # Since heapq is a min-heap, we use negative counts to simulate a max-heap
        max_heap = [-count for count in task_counts.values()]
        heapq.heapify(max_heap)

        # Queue to store the count of a task and the time it can be served again
        queue = deque()

        # Each interval represents a unit of time, so we start at time = 0
        time = 0

        # Continue processing until all tasks are completed
        while max_heap or queue:
            # Increase the time to indicate a cycle has passed
            time += 1

            # Check if there are tasks available in max_heap
            if max_heap:
                # Pop the task with the highest frequency (most negative value)
                # Add 1 because we're using negative values to maintain a max-heap
                count = 1 + heapq.heappop(max_heap)

                # If count is not zero, that means the task still needs to be worked on
                if count:
                    # Add this task to the queue with the time when it can be processed again
                    # The reprocessing time will be unique for each task based on the cooldown period `n`
                    queue.append([count, time + n])

            # After the current time interval, check if the task in the queue can be processed
            # If so, re-add the task to the heap to be considered for processing again
            if queue and queue[0][1] == time:
                # Re-add the task to the heap if it's ready to be processed again
                heapq.heappush(max_heap, queue.popleft()[0])

        return time
