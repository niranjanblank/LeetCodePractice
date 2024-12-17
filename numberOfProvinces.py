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


class Solution1:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # in this method we will keep visited_cities list

        visited_cities = [False]*len(isConnected)
        province = 0

        def dfs(city):
            # mark the city as visited
            visited_cities[city] = True
            # in the dfs function we will go through all the adjacent cities to the city
            for adj_city in range(len(isConnected)):
                # if there is a connection between adj_city and city, and adj_city isnt visited,
                # we visit adj_city and find all the cities connected to them using dfs and visit them
                if isConnected[city][adj_city] and not visited_cities[adj_city]:
                    dfs(adj_city)
                # checking if this city is connected to the current city or if its alrerady visited

        # going through all the visited_cities,
        for city in range(len(isConnected)):
            # if the city isnt visited, it means its in a new province,
            # so we will run dfs to find all the cities that are connected to this city 
            # and marking them as visited, when we go through the city again, we would know its already 
            # part of a province

            # for the first item in the visited_cities, it will be false, so we will run dfs to find all other cities that belong to this province
            if not visited_cities[city]:
                dfs(city)
                province+=1

        return province



# union find Solution
class UnionFind():
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_y] > self.rank[root_x]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x]+=1
    
    def connected(self,x,y):
        return self.find(x) == self.find(y)

class SolutionUnionFind:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # in this method we will go keep and visited_cities list
    
        n = len(isConnected)
        union_find = UnionFind(n)
        # initially, we assume there are n provinces, we will reduce the number of provinces 
        # if we find a city is already in the province
        provinces = n
        # iterating through isConnected to perform union, and find the provinces
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and not union_find.connected(i,j):
                    union_find.union(i,j)
                    provinces-=1
        
        return provinces
