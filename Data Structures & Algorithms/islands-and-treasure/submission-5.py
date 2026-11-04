class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])
        visited = [[False] * COL for _ in range(ROW)]

        def bfs(q, dis):
            while q:
                for _ in range(len(q)):
                    cr, cc = q.pop(0)
                    grid[cr][cc] = dis
                    for dr, dc in directions:
                        nr, nc = cr + dr, cc + dc
                        if 0 <= nr < ROW and 0 <= nc < COL and not visited[nr][nc] and grid[nr][nc] >0:
                            visited[nr][nc] = True
                            q.append((nr, nc))
                dis += 1


        q = []
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    q.append((r, c))
                    visited[r][c] = True

        bfs(q, 0)
        