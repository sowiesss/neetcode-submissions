class MinStack:

    def __init__(self):
        self.l = []
        self.mi = float('inf')


    def push(self, val: int) -> None:
        self.l.append((val, val - self.mi))   
        if val < self.mi:
            self.mi = val

        

    def pop(self) -> None:
        t = self.l[-1]
        if t[1] < 0:
            self.mi = t[0] - t[1]

        self.l.pop()


    def top(self) -> int:
        if self.l:
            return self.l[-1][0]
        return None
        

    def getMin(self) -> int:
        return self.mi
        
