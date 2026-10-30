class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

        

class WordDictionary:

    def __init__(self):
        self.trie = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.trie
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.endOfWord = True


    def search(self, word: str) -> bool:
        n = len(word)
        def dfs(i, node):
            curr = node
            for j in range(i, n):
                if word[j] == '.':
                    for child in curr.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    if word[j] in curr.children:
                        curr = curr.children[word[j]]
                    else:
                        return False
            return curr.endOfWord

        return dfs(0, self.trie)
