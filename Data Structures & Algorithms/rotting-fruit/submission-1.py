class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        q = []
        cnt = 0

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 1:
                    cnt += 1

        time = 0
        while cnt:
            flag = False
            for r in range(ROW):
                for c in range(COL):
                    if grid[r][c] == 2:
                        for dr, dc in directions:
                            nr, nc = dr + r, dc + c
                            if 0 <= nr < ROW and 0 <= nc < COL and grid[nr][nc] == 1:       
                                grid[nr][nc] = 3
                                cnt -= 1
                                flag = True
            if not flag:
                return -1

            for r in range(ROW):
                for c in range(COL):
                    if grid[r][c] == 3:
                        grid[r][c] = 2

            time += 1

        return time if not cnt else -1