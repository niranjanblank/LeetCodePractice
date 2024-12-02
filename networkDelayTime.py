class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Time Complexity: O(ElogE)
        # Sapce Complexity: O(V+E)
        # creating adjacency list
        adj = defaultdict(list)
        for u,v,w in times:
            adj[u].append((v,w))

        # heap to get the closest nodes, init it with the starting node
        minHeap = [(0,k)] # stores (path_length, node number)
        heapq.heapify(minHeap)
        # to store the shortest total signal
        t=0
        
        # keep track of all the visited nodes
        visited = set()
        while minHeap:
            # get the closest node
            w1, n1 = heapq.heappop(minHeap)

            # checking if its visited
            # if its visited, continue to next node
            if n1 in visited:
                continue
            # shortest path till current node
            t = max(t,w1)

            visited.add(n1)
            for n2, w2 in adj[n1]:
                if n2 not in visited:
                    # add the nodes adjacent to n1 to the heap to get the closest node
                    # to get total path we do w1+w2, as w1 gives total path till n1, and w1+w2 gives
                    # total path till n2 through n1
                    heapq.heappush(minHeap,(w1+w2,n2))
        
        # if visited has length of n, all the nodes will have been reached
        return t if len(visited) == n else -1
