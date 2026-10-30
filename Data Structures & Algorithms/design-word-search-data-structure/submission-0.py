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
        curr = self.trie
        for i, c in enumerate(word):
            if c == '.':
                for k, n in curr.children.items():
                    res = n.search(word[i + 1:])
                    if res:
                        return True
            else:
                if c in curr.children:
                    curr = curr.children[c]
                else:
                    return False
        return curr.endOfWord



class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

    def search(self, word: str) -> bool:
        curr = self
        for i, c in enumerate(word):
            if c == '.':
                for k, n in curr.children.items():
                    res = n.search(word[i + 1:])
                    if res:
                        return True
            else:
                if c in curr.children:
                    curr = curr.children[c]
                else:
                    return False
        return curr.endOfWord
