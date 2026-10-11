class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        prf = [101] * n
        suf = [0] * n
        prf[0] = prices[0]
        suf[-1] = prices[-1]

        for i in range(1, n):
            prf[i] = min(prices[i], prf[i - 1])
            if i < n - 1:
                suf[-i - 1] = max(prices[- i - 1], suf[-i]) 
        
        suf[0] = max(suf[1], prices[0])

        p = []
        for i in range(n):
            p.append(suf[i] - prf[i])
        
        ma = max(p)
        if ma > 0: 
            return ma
        return 0


