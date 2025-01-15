"""
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if (endWord not in wordList) or (beginWord == endWord):
                    return 0

        letters = "abcdefghijklmnopqrstuvwxyz"
        
        queue = deque()
        queue.append(beginWord)
        visited = set()
        steps = 0


        while queue:

            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return steps + 1
               
                for c in letters:
                    for i in range(len(beginWord)):
                        temp_word = word[:i] + c + word[i+1:]
                        if temp_word not in visited and temp_word in wordList:
                            queue.append(temp_word)
                            visited.add(word)

            steps+=1
        
        return 0


class Solution2:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Time Complexity : O(n*m^2)
        # Space Complexity:  O(n*m^2)

        wordList = set(wordList)
        if (endWord not in wordList) or (beginWord == endWord):
                    return 0

        # create adjacency list
        neigh = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neigh[pattern].append(word)

        
        queue = deque()
        queue.append(beginWord)
        visited = set()
        steps = 0

        while queue:

            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return steps + 1
               
                for i in range(len(beginWord)):
                    temp_word = word[:i] + "*" + word[i+1:]
                    
                    for i_word in neigh[temp_word]:
                        if i_word not in visited:
                            queue.append(i_word)
                            visited.add(i_word)
    
            steps+=1
        
        return 0
