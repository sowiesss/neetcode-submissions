class Tree:
    def __init__(self, size, list):
        self.l = list
        self.n = size
        self.MAX = 10 ** 5 + 1

        while(self.n & self.n - 1):
            self.n += 1
            self.l.append(self.MAX)

        self.tree = [0] * (self.n * 2)
        self.build()


    def build(self):
        for i in range(self.n):
            self.tree[self.n + i] = i
        for i in range(self.n - 1, 0, -1):
            a = self.tree[2 * i]
            b = self.tree[2 * i + 1]
            self.tree[i] = a if self.l[a] <= self.l[b] else b
    

    def query(self, ql, qr):
        return self._query(1, 0, self.n - 1, ql, qr)

    
    def _query(self, node, l, r, ql, qr):
        if ql <= l and qr >= r:
            return self.tree[node]
        
        if ql > r or qr < l: # l, r does not contribute to quried interval
            return self.MAX

        a = self._query((node << 1), l, (l + r) >> 1, ql, qr)
        b = self._query((node << 1) + 1, ((l + r) >> 1) + 1, r, ql, qr)

        if a == self.MAX:
            return b
        if b == self.MAX:
            return a

        return a if self.l[a] <= self.l[b] else b # return index



class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        t = Tree(n, heights)

        return self.getMaxArea(heights, t, 0, n - 1)

    
    def getMaxArea(self, heights, tree, l, r):
        if l > r:
            return 0
        if l == r:
            return heights[l]

        minInd = tree.query(l, r)

        return max(
            self.getMaxArea(heights, tree, l, minInd - 1), 
            self.getMaxArea(heights, tree, minInd + 1, r), 
            (r - l + 1) * heights[minInd]
        )

        
        