class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        diagnal1 = [False] * (2 * n - 1)
        diagnal2 = [False] * (2 * n - 1)
        col = [False] * n
        board = ["." * n for _ in range(n)]
        res = []

        def backtrack(row):
            if row == n:
                res.append(board.copy())
            
            for i in range(n):
                if col[i] or diagnal1[row + i] or diagnal2[row - i + n - 1]:
                    continue
                board[row] = board[row][:i] + 'Q' + board[row][i + 1:]
                diagnal1[row + i] = True
                diagnal2[row - i + n - 1] = True
                col[i] = True
                backtrack(row + 1)
                board[row] = "." * n
                diagnal1[row + i] = False
                diagnal2[row - i + n - 1] = False
                col[i] = False

        backtrack(0)
        return res


        