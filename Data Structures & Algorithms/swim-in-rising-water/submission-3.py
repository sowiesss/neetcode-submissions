class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        minh = maxh = grid[0][0]
        for r in range(n):
            maxh = max(maxh, max(grid[r]))
            minh = min(minh, min(grid[r]))


        def dfs(r, c, t):
            if r >= n or c >= n or r < 0 or c < 0 or visited[r][c] or grid[r][c] > t:
                return False

            if r == n - 1 and c == n - 1:
                return True
            visited[r][c] = True
            return (
                dfs(r + 1, c, t) or
                dfs(r - 1, c, t) or
                dfs(r, c + 1, t) or
                dfs(r, c - 1, t)
            )

        l, r = minh, maxh
        while l < r:
            m = (l + r) // 2
            if dfs(0, 0, m):
                r = m
            else:
                l = m + 1
            visited = [[False] * n for _ in range(n)]

        return r
            