class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(chosen, start):
            res.append(chosen.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                chosen.append(nums[i])
                backtrack(chosen, i + 1)
                chosen.pop()

        backtrack([], 0)
        return res