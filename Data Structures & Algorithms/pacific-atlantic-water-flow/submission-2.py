class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific = []
        atlantic = []
        
        def bfs(source, visit):
            while source:
                for _ in range(len(source)):
                    r, c = source.pop(0)
                    visit[r][c] = True
                    for dr, dc in directions:
                        nr, nc = dr + r, dc + c
                        if 0 <= nr < ROW and 0 <= nc < COL and heights[nr][nc] >= heights[r][c] and not visit[nr][nc]:
                            source.append((nr, nc))
                

        for r in range(ROW):
            pacific.append((r, 0))
            atlantic.append((r, COL -1))

        for c in range(COL):
            pacific.append((0, c))
            atlantic.append((ROW - 1, c))

        pac = [[False] * COL for _ in range(ROW)]
        atl = [[False] * COL for _ in range(ROW)]
        bfs(pacific, pac)
        bfs(atlantic, atl)

        res = []
        for r in range(ROW):
            for c in range(COL):
                if pac[r][c] and atl[r][c]:
                    res.append([r, c])

        return res
