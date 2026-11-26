class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l, r = 0, -1
        n = len(nums)
        maxl = 0
        ma = -math.inf
        res = 1
        for i in range(n):

            if nums[i] >= 1:
                res *= nums[i]
                r = i
            else:
                maxl = max(maxl, r - l + 1)
                l = i + 1
                ma = max(res, ma)
                res = 1

        return ma if maxl > 0 else max(nums)
