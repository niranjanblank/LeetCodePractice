"""
997. Find the Town Judge
Solved
Easy
Topics
Companies
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

 

Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1
 

Constraints:

1 <= n <= 1000
0 <= trust.length <= 104
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
"""


class Solution1:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Time Complexity: O(m+n), m = length of trust
        # Space Complexity: O(m+n), m = length of trust
        adj_in = defaultdict(list)
        adj_out = defaultdict(list)
        for t in trust:
            adj_in[t[1]].append(t[0])
            adj_out[t[0]].append(t[1])
        for i in range(1,n+1):
            if len(adj_in[i]) == n-1 and len(adj_out[i]) == 0:
                return i
        return -1

class Solution2:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Time Complexity: O(m+n)
        # Space Complexity: O(2(n+1)) = O(n)


        indegree = [0]*(n+1)
        outdegree = [0]*(n+1)
        for a,b in trust:
            indegree[b]+=1
            outdegree[a]+=1
        print(indegree, outdegree)

        for i in range(1,len(indegree)):
            if outdegree[i] == 0 and indegree[i] == n-1:
                return i
        
        return -1
