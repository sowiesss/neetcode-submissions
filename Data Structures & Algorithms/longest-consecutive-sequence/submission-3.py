class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums.sort()
        res, curr, streak, i = 0, nums[0], 0, 0
        while i < len(nums):
            if nums[i] != curr:
                streak = 0
                curr = nums[i]
            
            streak += 1
            res = max(streak, res)

            while i  < len(nums) and nums[i] == curr:
                i += 1
            curr += 1
        return res
        