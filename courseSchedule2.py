"""
210. Course Schedule II
Medium
Topics
Companies
Hint
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]


Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
"""


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preq_map = {i: [] for i in range(numCourses)}

        # filling the requirements in preq_map
        for preq in prerequisites:
            preq_map[preq[0]].append(preq[1])

        # we will keep two hashsets
        # one to keep track of the visited courses
        # a course could be added to the visited set if it can be scheduled, and doesnt belong to a cycle
        visited = set()
        # another to keep track cycle for checking if there exist a cycle
        cycle = set()  # if ever a cycle is formed, the courses cant be scheduled and

        output = []

        # setting a dfs method for finding courses
        def dfs(curr_cour):
            # if the cur_cour is already in a cycle, it means it forms a cycle and cannot be scheduled
            if curr_cour in cycle:
                return False

            # if the curr_cour is in visited, means its already processed and is already scheduled so we just skip
            if curr_cour in visited:
                return True

            # if we reach this point, then it isnt in cycle and hasnt been processed yet
            # add it to the cycle
            cycle.add(curr_cour)
            # now we need to check its its prerequisities can be scheduled
            for cour in preq_map[curr_cour]:
                # if any of its prerequisitis cannot be completed, we return false for the curr_cour as well
                if not dfs(cour): return False

            # if we reach here, it means the course can be completed, so we add it to visited set and output
            visited.add(curr_cour)
            output.append(curr_cour)
            cycle.remove(curr_cour)
            # preq_map[curr_cour] = []

            return True

        # now running the dfs
        for cour in range(numCourses):
            if not dfs(cour):
                return []

        return output
