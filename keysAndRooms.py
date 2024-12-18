"""
841. Keys and Rooms
"""
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        # set to keep track of all the visited nodes
        visited = set()

        def dfs(curr):
            # if already visited, skip
            if curr in visited:
                return
            # mark as visited
            visited.add(curr)

            # check if the neighboursr are visited, if not add them to visit
            for neigh in rooms[curr]:
                dfs(neigh)
            
        # run the dfs
        dfs(0)
    
        # if all nodes are visited then its length is equal to rooms
        return len(visited)==len(rooms)
