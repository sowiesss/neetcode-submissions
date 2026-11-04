class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):
            if grid[r][c] < 0:
                return -1
            if not grid[r][c]:
                return 0
            if grid[r][c] < INF:
                return grid[r][c]

            v = INF
            grid[r][c] = -2
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= ROW or nc >= COL or grid[nr][nc] < 0:
                    continue
                dis = dfs(nr, nc)
                if dis >= 0:
                    v = min(v, dis + 1)

            grid[r][c] = v
            return v

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == INF:
                    dfs(r, c)
                    
        
