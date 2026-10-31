class TrieNode:
    def __init__(self):
        self.children = {}
        self.idx = -1
        self.refs = 0


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.row = len(board)
        self.col = len(board[0])
        self.board = board
        self.words = words

        trie = TrieNode()
        for i, w in enumerate(words):
            curr = trie
            for c in w:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
                curr.refs += 1
            curr.idx = i

        self.res = set()
        
        for r in range(self.row):
            for c in range(self.col):
                self.dfs(r, c, trie)

        return list(self.res)
    

    def dfs(self, r, c, trie) -> int:
        if r < 0 or c < 0 or r >= self.row or c >= self.col or self.board[r][c] == '*' or self.board[r][c] not in trie.children:
            return 0
        
        temp = self.board[r][c]
        self.board[r][c] = '*'
        parent = trie
        trie = trie.children[temp]
        found = 0

        if trie.idx >= 0:
            self.res.add(self.words[trie.idx])
            trie.idx = -1
            found += 1

        cnt = 0
        cnt += self.dfs(r + 1, c, trie)
        cnt += self.dfs(r - 1, c, trie)
        cnt += self.dfs(r, c - 1, trie)
        cnt += self.dfs(r, c + 1, trie)

        found += cnt
        trie.refs -= found
        if trie.refs == 0:
            parent.children.pop(temp)
        self.board[r][c] = temp

        return found
