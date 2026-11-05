class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        q = []        

        for r in range(ROW):
            if board[r][0] == 'O':
                q.append((r, 0))
            if board[r][COL - 1] == 'O':
                q.append((r, COL - 1))

        for c in range(COL):
            if board[0][c] == 'O':
                q.append((0, c))
            if board[ROW - 1][c] == 'O':
                q.append((ROW - 1, c))

        while q:
            r, c = q.pop(0)
            board[r][c] = 'T'
            for dr, dc in directions:
                nr, nc = dr + r, dc +c
                if 0 <= nr < ROW and 0 <= nc < COL and board[nr][nc] == 'O':
                    q.append((nr, nc))
        

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'
                
