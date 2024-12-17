class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # time complexity: O(V+E)
        # space complexity: O(V)
        cycle_nodes = set() # keep track of the nodes that lead to cycle
        cycle = set() # keep track of current recursion stack
        visited = set() # keep track of all the nodes that have been processed completely
        # to visit all the paths from current node
        def dfs(curr):
            # if this dfs returns False, we encounter cycle
            # else we dont encounter cycle
            
            # check if the node is part of cycle
            if curr in cycle:
                return False
            # check if visited
            if curr in visited:
                return True
            
            # add the node to the cycle stack
            cycle.add(curr)
            # if node isnt in cyle and isnt visited, we run dfs on its neighbours
            for neigh in graph[curr]:
                # if this neigh is already in cycle,
                # dfs will return false, so we can add curr to cycle_node as it will lead to cycle
                if not dfs(neigh):
                    cycle_nodes.add(curr)
                    # cycle detected here so we return False
                    return False  
                
            # mark the node as visited
            visited.add(curr)
            # remove it from the cycle recursion stack
            cycle.remove(curr)

            # if we reach here it means wo dont encounter cycle from curr
            return True
        for node in range(len(graph)):
            # we go through each node
            if node not in visited:
                dfs(node)
    
        return [i for i in range(len(graph)) if i not in cycle_nodes]

        
