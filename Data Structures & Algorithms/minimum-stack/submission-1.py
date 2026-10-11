class MinStack:

    def __init__(self):
        self.l = []
        self.minL = []

    def push(self, val: int) -> None:
        self.l.append(val)
        if ((self.minL and val <= self.minL[-1])
            or not self.minL):
            self.minL.append(val)
       

    def pop(self) -> None:
        self.minL.pop()
        self.l.pop()


    def top(self) -> int:
        if self.l:
            return self.l[-1]
        return None
        

    def getMin(self) -> int:
        return self.minL[-1] if self.minL else None
        
