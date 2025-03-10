"""
815. Bus Routes
Solved
Hard
Topics
Companies
You are given an array routes representing bus routes where routes[i] is a bus route that the ith bus repeats forever.

For example, if routes[0] = [1, 5, 7], this means that the 0th bus travels in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
You will start at the bus stop source (You are not on any bus initially), and you want to go to the bus stop target. You can travel between bus stops by buses only.

Return the least number of buses you must take to travel from source to target. Return -1 if it is not possible.

 

Example 1:

Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
Output: 2
Explanation: The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
Example 2:

Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target = 12
Output: -1
 

 

Constraints:

1 <= routes.length <= 500.
1 <= routes[i].length <= 105
All the values of routes[i] are unique.
sum(routes[i].length) <= 105
0 <= routes[i][j] < 106
0 <= source, target < 106
"""

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Time Complexity : O(N+E)
        # Space Complexity : O(N+E)
        stop_to_buses =  defaultdict(list)

        # fill this adj list to find all the buses accesible at a stop

        for bus_index,route in enumerate(routes):
            for stop in route:
                stop_to_buses[stop].append(bus_index)

        # queue to store stop and bus count to reach that stop
        # initially we start with source and 0 as bus count
        queue = deque()
        queue.append((source,0))

        # keep track of the bus and stops that have been visited
        visited_buses = set()
        visited_stops = set()
        visited_stops.add(source)
        while queue:

            for _ in range(len(queue)):
                stop, bus_count = queue.popleft()

                if stop == target:
                    return bus_count

                # now from this stop, we get into all the buses we can get 
                for bus in stop_to_buses[stop]:
                    # from this bus, add all the stops that can be reached and increase the bus count
                    # if the bus has been visited, we dont need to process it
                    if bus in visited_buses:
                        continue
                    # mark the bus as visited
                    visited_buses.add(bus)
                    for next_stop in routes[bus]:
                        if next_stop not in visited_stops:
                            queue.append((next_stop, bus_count+1))
                            visited_stops.add(next_stop)

        return -1

