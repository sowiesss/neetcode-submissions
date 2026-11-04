class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2 ** 31 - 1
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROW, COL = len(grid), len(grid[0])

        def dfs(r, c, dis):
            if (r < 0 or c < 0 or r >= ROW or c >= COL
                or grid[r][c] == -1):
                return

            if dis >= grid[r][c]:
                return

            grid[r][c] = dis

            for dr, dc in directions:
                dfs(r + dr, c + dc, dis + 1)

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    dfs(r, c, 0)