class Solution1:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # creating adjacency list
        adj = {src: [] for src, dst in tickets}

        tickets.sort()

        # filling the adjacency list
        for src, dst in tickets:
            adj[src].append(dst)
        
        res= ["JFK"]

        def dfs(src):
            # If the itinerary contains all tickets plus the starting point, we are done
            if len(res) == len(tickets) + 1:
                return True
            # If the current source has no outgoing flights, return False
            if src not in adj:
                # src doesnt have outgoing edges
                return False
            
            temp = list(adj[src])
            for i, v in enumerate(temp):
                # Add the destination to the result
                res.append(v)
                # Remove this destination from the adjacency list to mark it as visited
                adj[src].pop(i)
                 # Recursively perform DFS from the current destination
                if dfs(v): return True
                 # If this path doesn't lead to a valid itinerary, backtrack
                # Restore the destination to the adjacency list and remove it from the result
                adj[src].insert(i, v)
                res.pop()
        # Return False if no valid itinerary is found from this source
            return False
        # Start DFS from the starting airport "JFK"
        dfs("JFK")

        return res

#Hierholzer's Algorithm
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # creating adjacency list

        adj = defaultdict(list)
        res = []
        # filling the adjacency list
        for src, dst in sorted(tickets)[::-1]:
            adj[src].append(dst)

        def dfs(src):
            # while there are places that can be visited from src
            while adj[src]:
                dst = adj[src].pop()
                dfs(dst)
            res.append(src)
        
        dfs("JFK")

        return res[::-1]
