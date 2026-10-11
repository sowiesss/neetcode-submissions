class MinStack:

    def __init__(self):
        self.l = []
        self.mi = float('inf')
        self.nextMin = float('inf')

    def push(self, val: int) -> None:
        self.l.append(val)
        if val <= self.mi:
            self.nextMin = self.mi
            self.mi = val


    def pop(self) -> None:
        if self.l[-1] == self.mi:
            self.mi = self.nextMin
        self.l.pop()


    def top(self) -> int:
        if self.l:
            return self.l[-1]
        return None
        

    def getMin(self) -> int:
        return self.mi if self.mi != float('inf') else None
        
