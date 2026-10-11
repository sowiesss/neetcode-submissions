class SegmentTree:
    def __init__(self, size, arr):
        self.n = size
        while (self.n & (self.n - 1)) != 0: #increase to next power of 2, 7 - > 8
            self.n += 1
        self.build(size, arr)
    
    def build(self, size, arr):
        self.tree = [float('-inf')] * ( 2 * self.n)
        for i in range(size):
            self.tree[self.n + i] = arr[i] # build level 1 (leaves), self.n nodes
        for i in range(self.n - 1, 0, -1): # build parents and root (1, self.n - 1)
            self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1]) # self.tree[2*i], self.tree[2*i + 1]

    def query(self, l, r):
        res = float('-inf')
        l += self.n
        r += self.n # change index to leave index, original r included
        while l <= r: # if l, r = 8, 9, only 1 interation, i.e 1 leave is compared; if l, r = 8, 10, 2 interation, node 4 is compared - 8, 9's parent
            if l & 1: # l % 2 == 1, odd
                res = max(res, self.tree[l]) # l's parent is not included, only compare l
                l += 1 # go to l + 1' parent
            if r ^ 1:
                 # the leave left to it is included
                res = max(res, self.tree[r])
                r -= 1
            l >>= 1
            r >>= 1 # r // 2
        return res



class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        tree = SegmentTree(n, nums)
        res = []
        for i in range(n - k + 1):
            res.append(tree.query(i, i + k - 1)) 
        return res       