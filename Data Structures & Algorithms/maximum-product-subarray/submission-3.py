class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        pre, suf = 1, 1
        for i in range(n):
            if nums[i] == 0:
                pre, suf = 1, 1
                res = max(res, 0)
                continue
            pre *= nums[i]
            suf *= nums[n - 1 - i]
            res = max(res, pre, suf)
        
        return res
