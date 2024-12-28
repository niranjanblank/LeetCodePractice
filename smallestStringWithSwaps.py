"""
1202. Smallest String With Swaps
Solved
Medium
Topics
Companies
Hint
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.

 

Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination: 
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination: 
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"
 

Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
"""

class UnionFind:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n

    def find(self,x):
        if x!=self.root[x]:
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
                self.rank[root_x] += 1
     

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # Time Complexity: O((E+V)⋅α(V)+VlogV)
        # Space Complexity: O(V)
        s= list(s)
        uf = UnionFind(len(s))
        hashmap = defaultdict(list)
        # getting the connected components
        for pair in pairs:
            uf.union(pair[0], pair[1])

        for i in range(len(s)):
            component = uf.find(i)
            hashmap[component].append(i)
  

        for indices in hashmap.values():
            chars = sorted(s[i] for i in indices)

            # place the sorted character in location
            for idx, char in zip(indices, chars):
                s[idx] = char


        return "".join(s)
