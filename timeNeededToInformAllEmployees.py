"""
1376. Time Needed to Inform All Employees
"""

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        #Time Complexity : O(n)
        #Space Complexity: O(n)
        # create adjaceny list to create link manager with their employees
        adj_list = defaultdict(list)
        # filling the adj_list
        for i,emp in enumerate(manager):
            adj_list[emp].append(i)
        queue = deque()
        # adding the head and starting inform time 
        queue.append((headID, informTime[headID]))
        max_time = 0
        while queue:
            curr_emp, message_time = queue.popleft()
            max_time = max(max_time, message_time)
            # going through the adj list
            for item in adj_list[curr_emp]:
                if item in adj_list:
                    # the times are added here so as we account the time required to reach till this point
                    queue.append((item, message_time + informTime[item]))

        return max_time
