class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        visited = [[False] * COL for _ in range(ROW)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nc < 0 or nr >= ROW or nc >= COL:
                    return True
                elif visited[nr][nc] or board[nr][nc] == 'X':
                    continue
                else: 
                    res = dfs(nr, nc)
                    if res:
                        print(nr, nc)
                        return True

            return False


        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'O':
                    res = dfs(r, c)
                    if not res:
                        board[r][c] = 'X'
