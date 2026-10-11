class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            col_seen = set()

            for j in board[i]:
                seen = set()
                if j == '.' : continue
                if j not in seen:
                    seen.add(j)
                else:
                    return False

            for j in range(9):
                if board[j][i] == '.' : continue
                if board[j][i] not in col_seen:
                    col_seen.add(board[j][i])
                else:
                    return False
                    
            if i in (0, 3, 6):
                for j in (0, 3, 6):
                    seen = set()
                    for col in range(3):
                        for row in range(3):
                            if board[i+row][j+col] == ".":
                                continue
                            if board[i+row][j+col] not in seen:
                                seen.add(board[i+row][j+col])
                            else:
                                print()
                                return False

        return True
                    