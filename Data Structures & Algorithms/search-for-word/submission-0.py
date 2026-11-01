class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.board = board
        self.word = word
        self.r = len(board)
        self.c = len(board[0])
        for r in range(self.r):
            for c in range(self.c):
                res = self.backtrack(r, c, 0)
                if res:
                    return True
        
        return False


    def backtrack(self, r, c, i):
        if i >= len(self.word):
            return True

        if r < 0 or c < 0 or r >= self.r or c >= self.c or self.board[r][c] != self.word[i]:
            return False
        
        neighbor = (self.backtrack(r - 1, c, i + 1)
                    or self.backtrack(r + 1, c, i + 1)
                    or self.backtrack(r, c - 1, i + 1)
                    or self.backtrack(r, c + 1, i + 1)
                )

        return neighbor