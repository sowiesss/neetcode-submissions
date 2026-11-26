class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]
        pre, suf = 1, 1
        for i in range(n):
            if nums[i] == 0:
                pre = 1
                res = max(res, 0)
            else:
                pre *= nums[i]
                res = max(res, pre)
            
            if nums[n - 1 - i] == 0:
                suf = 1
                res = max(res, 0)
            else:
                suf *= nums[n - 1 - i]
                res = max(res, suf)
        
        return res
