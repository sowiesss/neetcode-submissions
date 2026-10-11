class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        if n < 2:
            return [0]


        res = [0] * n
        for i in range(n - 2, -1, -1):
            j = i + 1
            while temperatures[j] <= temperatures[i]:
                if res[j]:
                    j += res[j]
                else:
                    res[i] = 0
                    break
            if temperatures[j] > temperatures[i]:
                res[i] = j - i
            
        return res


            
            
        