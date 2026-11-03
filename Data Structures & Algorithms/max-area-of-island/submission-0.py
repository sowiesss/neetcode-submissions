class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxA = 0
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or c >= COL or r >= ROW or not grid[r][c]:
                return 0
            
            a = 1
            grid[r][c] = 0
            a += dfs(r - 1, c)
            a += dfs(r + 1, c)
            a += dfs(r, c - 1)
            a += dfs(r, c + 1)

            return a

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]:
                    maxA = max(maxA, dfs(r, c))
        
        return maxA