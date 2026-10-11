class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        ma = 0
        l, r = 0, 1
        while r < n:
            if prices[r] <= prices[l]:
                l = r
            else:
                ma = max(prices[r] - prices[l], ma)
            r += 1

        return ma

