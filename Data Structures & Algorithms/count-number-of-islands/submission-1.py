class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0])
        
        def bfs(r, c):
            queue = [(r, c)]

            while queue:
                r, c = queue.pop(0)
                if r < m and r >= 0 and c < n and c >= 0 and grid[r][c] == '1':
                    grid[r][c] = '0'
                    queue.append((r - 1, c))
                    queue.append((r + 1, c))
                    queue.append((r, c - 1))
                    queue.append((r, c + 1))
                
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    bfs(r, c)
                    cnt += 1
        
        return cnt
