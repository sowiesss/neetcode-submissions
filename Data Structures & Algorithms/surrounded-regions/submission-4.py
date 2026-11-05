class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            board[r][c] = 'T'
            for dr, dc in directions:
                nr, nc = dr + r, dc +c
                if 0 <= nr < ROW and 0 <= nc < COL and board[nr][nc] == 'O':
                    dfs(nr, nc)
                    

        for r in range(ROW):
            if board[r][0] == 'O':
                dfs(r, 0)
            if board[r][COL - 1] == 'O':
                dfs(r, COL -1)

        for c in range(COL):
            if board[0][c] == 'O':
                dfs(0, c)
            if board[ROW - 1][c] == 'O':
                dfs(ROW - 1, c)

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
                
