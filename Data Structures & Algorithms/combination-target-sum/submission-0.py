class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(start, target, chosen):
            if target == 0:
                res.append(chosen.copy())
                return

            for i in range(start, len(nums)):
                if target - nums[i] < 0:
                    break
                chosen.append(nums[i])
                backtrack(i,  target - nums[i], chosen)
                chosen.pop()

        backtrack(0, target, [])
        return res
        