class DSU:
    def __init__(self, size):
        self.parent = [x for x in range(size)]
        self.size = [1] * size


    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    
    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False
        if self.size[p1] >= self.size[p2]:
            self.size[p1] += self.size[p2]
            self.parent[p2] = p1
        else:
            self.size[p2] += self.size[p1]
            self.parent[p1] = p2
        return True 



class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        dsu = DSU(n + 1)

        for s, e in edges:
            if not dsu.union(s, e):
                return [s, e]

        return []
