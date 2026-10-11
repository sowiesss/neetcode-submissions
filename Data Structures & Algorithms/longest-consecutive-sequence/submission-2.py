class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0

        nums.sort()
        res, curr, streak, i = 0, nums[0], 0, 0
        while i < len(nums):
            if nums[i] == curr:
                streak += 1
                res = max(streak, res)
            else:
                streak = 1
                curr = nums[i]
            while i  < len(nums) and nums[i] == curr:
                i += 1
            curr += 1
        return res
        