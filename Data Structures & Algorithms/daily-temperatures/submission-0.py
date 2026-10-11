class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n < 2:
            return [0]

        stk = [] # n - 1 ~ 1
        for i in range(n - 1, 0, -1):
            if not stk or temperatures[i] > stk[-1]:
                stk.append(i)

        res = []
        m = len(stk)
        for l in range(n - 1):
            index = m - 1
            r = stk[index]
            while index > 0 and r <= l:
                index -= 1
                r = stk[index]
            if not index:
                res.append(0)
            else: # r > l
                while index > 0 and temperatures[r] <=  temperatures[l]:
                    index -= 1
                    r = stk[index]
                if not index:
                    res.append(0)
                else:
                    res.append(r - l)
        res.append(0) # res[n - 1] is always 0
        return res

            
            
        