class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        ma = 0
        buy = prices[0]

        for i in range(1, n):
            if prices[i] <= buy:
                buy = prices[i]
            else:
                profit = prices[i] - buy
                ma = max(ma, profit)
        
        return ma

