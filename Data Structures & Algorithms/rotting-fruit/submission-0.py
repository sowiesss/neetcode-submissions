class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = []
        cnt = 0
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    cnt += 1

        time = 0
        while q and cnt:
            for _ in range(len(q)):
                r, c = q.pop(0)
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 1:       
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        cnt -= 1
            time += 1

        return time if not cnt else -1