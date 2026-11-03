class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0])
        direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        dsu = DSU(m * n)

        def index(r, c):
            return r * n + c
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    cnt += 1
                    for dr, dc in direction:
                        nr = dr + r
                        nc = dc + c
                        if (nr < 0 or nc < 0 or nr >= m or nc >= n or grid[nr][nc] == '0'):
                            continue
                        if dsu.union(index(nr, nc), index(r, c)):
                            cnt -= 1
                    
        return cnt


class DSU:
    def __init__(self, n):
        self.parent = [ _ for _ in range(n)]
        self.size = [1] * n

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

