"""
1101. Earliest Moment When Everyone Becomes Friends
"""
class UnionFind:
    def __init__(self,n):
        self.root = [i for i in range(n)]
        self.rank = [1]*n

    def find(self, x):
        if x != self.root[x]:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            # if they are already connected return False
            return False
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
            elif self.rank[root_y] > self.rank[root_x]:
                self.root[root_x] = root_y
            else:
                self.root[root_y] = root_x
                self.rank[root_x] != 1
        # if connected successfully, return  True
        return True
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        num_connected_components = n
        logs = sorted(logs)
        union_find = UnionFind(n)
        for item in logs:
            if union_find.union(item[1], item[2]):
                num_connected_components -= 1
            # if num_connected_components becomes 1, it means every one is friend, so return the time stamp
            if num_connected_components == 1:
                return item[0]
        # if the num_connected_components couldnt be 1, then all counldnt be friends so return -1
        return -1
