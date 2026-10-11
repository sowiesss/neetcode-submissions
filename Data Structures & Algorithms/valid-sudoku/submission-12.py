class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [0] * 9
        row = [0] * 9
        square = [0] * 9

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.': continue
                val = int(val)
                if (1 << val & col[j] or 
                    1 << val & row[i] or
                    1 << val & square[(i//3) * 3 + j//3]):
                    return False
                col[j] |= 1 << val
                row[i] |= 1 << val
                square[(i//3) * 3 + j//3] |= 1 << val

        return True
                    