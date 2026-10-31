class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        R, C = len(board), len(board[0])
        res = []

        def backtrack(r, c, i, word):
            if i == len(word):
                return True

            if (r < 0 or c < 0 or r >= R or c >= C or board[r][c] != word[i]):
                return False

            board[r][c] = '*'
            neighbor = (backtrack(r + 1, c, i + 1, word)
                    or backtrack(r - 1, c, i + 1, word)
                    or backtrack(r, c + 1, i + 1, word)
                    or backtrack(r, c - 1, i + 1, word))
            board[r][c] = word[i]
            return neighbor

        for w in words:
            flag = False
            for r in range(R):
                if flag:
                    break
                for c in range(C):
                    if board[r][c] != w[0]:
                        continue
                    if backtrack(r, c, 0, w):
                        res.append(w)
                        flag = True
                        break

        return res

        