class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # adj list to store red path from a node to another node
        red_list = defaultdict(list)
        blue_list = defaultdict(list)

        for item in redEdges:
            red_list[item[0]].append(item[1])
            
        for item in blueEdges:
            blue_list[item[0]].append(item[1])

        queue = deque()

        result = [-1]*n
        result[0] = 0

        queue.append([0,0,None]) # [curr_node, length to get to this node from 0, color of prev path]

        # keep track of visited nodes
        visited = set()
        visited.add((0,None))

        while queue:
            node, length, edge_color = queue.popleft()

            # if the path has not been reached before, set its length
            if result[node] == -1:
                result[node] = length
        
            # going to the red path from curr node if prev path wasnt red
            if edge_color != "red":
                for nei in red_list[node]:
                    if (nei, "red") not in visited:
                        queue.append([nei, length+1,"red"])
                        visited.add((nei,"red"))
            
            # going to blue path from curr node if prev path wasnt blue
            if edge_color != "blue":
                for nei in blue_list[node]:
                    if (nei, "blue") not in visited:
                        queue.append([nei, length+1, "blue"])
                        visited.add((nei,"blue"))
            
        return result
