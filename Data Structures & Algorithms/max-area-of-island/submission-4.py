class DSU:
    def __init__(self, size):
        self.p = [ _ for _ in range(size)]
        self.size = [1] * size

    def find(self, node):
        if self.p[node] != node:
            self.p[node] = self.find(self.p[node])
        return self.p[node]

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return
        if self.size[p1] >= self.size[p2]:
            self.size[p1] += self.size[p2]
            self.p[p2] = p1
        else:
            self.size[p2] += self.size[p1]
            self.p[p1] = p2
            
    def getSize(self, node):
        p = self.find(node)
        return self.size[p]


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxA = 0
        ROW, COL = len(grid), len(grid[0])
        dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        dsu = DSU(ROW * COL)

        def index(r, c):
            return r * COL + c
        
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]:
                    for dr, dc in dir:
                        nr, nc = dr + r, dc + c
                        if nr < 0 or nr >= ROW or nc < 0 or nc >= COL or not grid[nr][nc]:
                            continue
                        dsu.union(index(r, c), index(nr, nc))
                    maxA = max(maxA, dsu.getSize(index(r, c)))
        
        return maxA