class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # creating an adjacency list to store the relation between characters
        adj = {c:set() for word in words for c in word}
        
        # filling up the list
        for i in range(len(words)-1):
            # taking two words at a time
            w1, w2 = words[i], words[i+1]
            # comparing the two words to get relation among the character
            min_len = min(len(w1),len(w2))
            # if two words are similar towards certain lenghth, and longer word comes before shorter word
            # the claim of alien dictionary becomes false and we return empty string
            if w1[:min_len] == w2[:min_len] and len(w2)<len(w1):
                return ""

            # comparing each char and adding the relation to adjacency list
            for j in range(min_len):
                # the the char at certain location arent equal,
                # then the letter from w1 comes before letter from w2
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # this will store a dictionary value like {{char: bool}}
        # if the bool is false, it means the char is visited but isnt in the current path
        # else, it means the char is visited and is in the current path
        visited = {}
        # to keep track of the order
        res = []

        def dfs(c):
            # if the item is visited, return the state of the item
            if c in visited:
                return visited[c]
            
            # mark it as visited and in current path
            visited[c] = True

            # go through all the relations of char c
            for nei in adj[c]:
                # if we get true here it means we have encountered a loop
                if dfs(nei):
                    return True
            
            # remove c from the current path
            visited[c] = False
            # add c to the result
            res.append(c)

        for c in adj:
            # start the dfs and check for loop
            if dfs(c):
                return ""
        return "".join(res[::-1])
        
