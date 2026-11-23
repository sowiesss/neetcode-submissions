class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        presum = [0] * n
        presum[0], presum[1], presum[2] = nums[0], nums[1], nums[0] + nums[2]
        for i in range(3, n):
            presum[i] = nums[i] + max(presum[i - 2], presum[i - 3])

        return max(presum[n - 1], presum[n - 2])
            