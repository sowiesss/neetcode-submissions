class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        ma, mi = 1, 1
        for n in nums:
            tma = ma * n
            tmi = mi * n
            ma = max(n, tma, tmi)
            mi = min(n, tma, tmi)
            res = max(ma, res)
        return res
