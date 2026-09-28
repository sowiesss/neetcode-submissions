class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(n-1):
            j = n - i - 1
            prefix[i + 1] = prefix[i] * nums[i]
            suffix[j - 1] = suffix[j] * nums[j] 

        res = []
        for i in range(n):
            res.append(prefix[i] * suffix[i])
        
        return res





            
            