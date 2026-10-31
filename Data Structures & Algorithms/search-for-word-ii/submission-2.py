class TrieNode:
    def __init__(self):
        self.children = {}
        self.eow = False


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.row = len(board)
        self.col = len(board[0])
        self.board = board

        trie = TrieNode()
        for w in words:
            curr = trie
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.eow = True

        self.res = set()
        
        for r in range(self.row):
            for c in range(self.col):
                self.dfs(r, c, trie, [])

        return list(self.res)
        
    

    def dfs(self, r, c, trie, chars):
        if r < 0 or c < 0 or r >= self.row or c >= self.col or self.board[r][c] == '*' or self.board[r][c] not in trie.children:
            return 
        
        temp = self.board[r][c]
        self.board[r][c] = '*'
        trie = trie.children[temp]
        chars.append(temp)
        if trie.eow:
            self.res.add(''.join(chars))

        self.dfs(r + 1, c, trie, chars) 
        self.dfs(r - 1, c, trie, chars)
        self.dfs(r, c - 1, trie, chars)
        self.dfs(r, c + 1, trie, chars)
        
        self.board[r][c] = temp
