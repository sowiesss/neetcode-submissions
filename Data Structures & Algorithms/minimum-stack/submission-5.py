class MinStack:

    def __init__(self):
        self.l = []
        self.mi = 2 ^ 31 - 1


    def push(self, val: int) -> None:
        if val < self.mi:
            self.mi = val
        self.l.append((val, self.mi))   


    def pop(self) -> None:
        self.l.pop()
        if self.l:
            self.mi = self.l[-1][1]


    def top(self) -> int:
        if self.l:
            return self.l[-1][0]
        return None
        

    def getMin(self) -> int:
        return self.mi
        
