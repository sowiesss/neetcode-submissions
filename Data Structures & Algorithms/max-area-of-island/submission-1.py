class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxA = 0
        ROW, COL = len(grid), len(grid[0])

        def bfs(r, c):
            q = [(r, c)]
            a = 0
            while q:
                row, col = q.pop(0)

                if row < 0 or col < 0 or col >= COL or row >= ROW or not grid[row][col]:
                    continue

                grid[row][col] = 0
                a += 1
                q.append((row - 1, col))
                q.append((row + 1, col))
                q.append((row, col - 1))
                q.append((row, col + 1))
            return a

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]:
                    maxA = max(maxA, bfs(r, c))
        
        return maxA