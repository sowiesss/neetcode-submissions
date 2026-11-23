class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        presum = [0] * n
        presum[0], presum[1] = nums[0], max(nums[0], nums[1]) 
        for i in range(2, n):
            presum[i] = max(nums[i] + presum[i - 2], presum[i - 1])
        return presum[-1]
            