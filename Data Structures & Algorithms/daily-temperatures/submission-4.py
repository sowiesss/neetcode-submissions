class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n < 2:
            return [0]

        stk = []
        res = [0] * n
        for i in range(n - 1, -1, -1):
            while stk and temperatures[stk[-1]] <= temperatures[i]:
                stk.pop()    
            if stk:
                res[i] = stk[-1] - i
            stk.append(i)           
        return res

            
            
        