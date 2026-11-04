class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])
       

        def bfs(r, c):
            q = [(r, c)]
            visited = [[False] * COL for _ in range(ROW)]
            visited[r][c] = True
            step = 0
            while q:
                for _ in range(len(q)):
                    cr, cc = q.pop(0)
                    if grid[cr][cc] == 0:
                        return step
                    for dr, dc in directions:
                        nr, nc = dr + cr, dc + cc
                        if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] >= 0 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                step += 1
            return INF

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)
        
