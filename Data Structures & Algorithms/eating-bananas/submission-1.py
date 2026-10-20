class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        ma = max(piles)
        res = ma

        while left <= ma:
            mid = left + (ma - left) // 2
            t = 0
            for p in piles:
                t += math.ceil(p / mid)

            if t <= h:
                ma = mid - 1
                res = mid
            else:
                left = mid + 1

        return res
