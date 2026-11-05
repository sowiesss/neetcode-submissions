class DSU:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size


    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]


    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if p1 == p2:
            return False
        if self.size[p1] >= self.size[p2]:
            self.size[p1] += self.size[p2]
            self.parent[p2] = p1
        else:
            self.size[p2] += self.size[p1]
            self.parent[p1] = p2
        return True


    def connected(self, n1, n2):
        return self.find(n1) == self.find(n2)



class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW, COL = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dsu = DSU(ROW * COL + 1)
        
        def index(r, c):
            return r * COL + c      

        dummy = index(ROW, 0)
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] != 'O':
                    continue
                ind = index(r, c)
                if r == 0 or c == 0 or r == ROW - 1 or c == COL - 1:
                    dsu.union(ind, dummy)
                else:
                    for dx, dy in directions:
                        nr, nc = r + dx, c + dy
                        if board[nr][nc] == "O":
                            dsu.union(ind, index(nr, nc))

        for r in range(ROW):
            for c in range(COL):   
                if board[r][c] == 'O' and not dsu.connected(dummy, index(r, c)):
                    board[r][c] = 'X'
