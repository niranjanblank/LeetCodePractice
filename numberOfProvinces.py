"""

547. Number of Provinces
Solved
Medium
Topics
Companies
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        def dfs(city):
            # mark the city as connected
            visited[city] = True
            # Checking if city is connected to other adjacent cities or not
            for adjacent_city in range(len(isConnected)):
                # checking if the there is link between the city and adjacent city
                if isConnected[city][adjacent_city] and not visited[adjacent_city]:
                    dfs(adjacent_city)

        # currenyly assuming of the cities are visited
        visited = [False]*len(isConnected)
        provinces = 0
        for city in range(len(isConnected)):
            # if the city hasnt been visited previously we visit it and increase 
            # the nunber of provinces
            if not visited[city]:
                dfs(city)
                provinces+=1

        return provinces