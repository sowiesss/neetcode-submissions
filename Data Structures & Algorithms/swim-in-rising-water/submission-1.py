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
        if self.size[p1] > self.size[p2]:
            p1, p2 = p2, p1
        
        self.size[p2] += self.size[p1]
        self.parent[p1] = p2
        return True



class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dsu = DSU(n * n)
        edge = []
        

        for r in range(n):
            for c in range(n):
                edge.append((grid[r][c], r, c))

        edge.sort()

        def id(r, c):
            return r * n + c

        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        sid = id(0, 0)
        did = id(n - 1, n - 1)
        for t, r, c in edge:
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr >= n or nc >= n or nc < 0 or nr < 0 or grid[nr][nc] > t:
                    continue
                if dsu.union(id(r,c), id(nr, nc)):
                    if dsu.find(sid) == dsu.find(did):
                        return t

        return 0








