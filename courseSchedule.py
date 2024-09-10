"""
207. Course Schedule
Medium
Topics
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # creating a hashmap to store prerequisite of all the courses

        # this creates empty map for all the courses
        preq_map = {i: [] for i in range(numCourses)}

        # filling the prerequisites
        for preq in prerequisites:
            # e.g preq = [0,1] 0 depends upton 1
            preq_map[preq[0]].append(preq[1])

        # keeping track of all the visited prerequisties to check for loop
        # if we try to find an item thats already in visited set, a loop is discovered and we cannot finish the course
        visited = set()

        # dfs function to check if each of the nodes are completeable
        # we take current course as the input
        def dfs(curr_cour):
            # if the curr_cour is already visited return false
            if curr_cour in visited:
                return False

            # if the curr_cour doesnt depend on anything, it is completable and we return True
            if preq_map[curr_cour] == []:
                return True

            # if we reach here, means the currr_cour isnt visited and its not complete yet
            # add it to the visited set
            visited.add(curr_cour)
            # loop through all the prerequisites of curr_cour and check if they can be completed
            for item in preq_map[curr_cour]:
                # if we get a false from any of its prerequisites, we return false as it cannot be completed
                if not dfs(item): return False

            # if all the prerequisites can be done, we change the prerequisite of curr_cour to []
            preq_map[curr_cour] = []
            # and remove it from visited
            visited.remove(curr_cour)

            return True

        # now running through each of the node to see if all the course are completable
        # we need to run this as they might be some courses that might not be related to each other
        # eg [[0,1][1,2][3,4][4,5]] , here completion of 0,1,2 wont ever depend on 3,4,5
        for cour in range(numCourses):
            # if any of the prereq isnt able to be completed return False
            if not dfs(cour): return False

        return True