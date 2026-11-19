class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]

        def dfs(r, c, t):
            if r >= n or c >= n or r < 0 or c < 0 or visited[r][c]:
                return math.inf

            t = max(t, grid[r][c])
            if r == n - 1 and c == n - 1:
                return t
            visited[r][c] = True
            time = min(
                dfs(r + 1, c, t),
                dfs(r - 1, c, t),
                dfs(r, c + 1, t),
                dfs(r, c - 1, t)
            )
            visited[r][c] = False
            return time

        return dfs(0, 0, 0)
            