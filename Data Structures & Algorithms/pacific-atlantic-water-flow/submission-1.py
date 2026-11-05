class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        pacific = set()
        atlantic = set()
        
        def dfs(r, c, res):
            res.add((r, c))
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if 0 <= nr < ROW and 0 <= nc < COL and heights[nr][nc] >= heights[r][c] and (nr, nc) not in res:
                    dfs(nr, nc, res)
                
        for r in range(ROW):
            dfs(r, 0, pacific)
            dfs(r, COL - 1, atlantic)
        
        for c in range(COL):
            dfs(0, c, pacific)
            dfs(ROW - 1, c, atlantic)

        res = []
        for r in range(ROW):
            for c in range(COL):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])

        return res
