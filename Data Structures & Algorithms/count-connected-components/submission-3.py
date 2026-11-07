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
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        cnt = n
        for v1, v2 in edges:
            if dsu.union(v1, v2):
                cnt -=1 
        
        return cnt
 

        