class PrefixTree:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if curr.children[ind] == 0:
                curr.children[ind] = TreeNode()
            curr = curr.children[ind]
        curr.isEnd = True


    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            ind = ord(c) - ord('a')
            if curr.children[ind] != 0:
                curr = curr.children[ind]
            else:
                return False
        return curr.isEnd


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            ind = ord(c) - ord('a')
            if curr.children[ind] != 0:
                curr = curr.children[ind]
            else:
                return False
        return True
        

class TreeNode:
    def __init__(self):
        self.children = [0] * 26
        self.isEnd = False
    