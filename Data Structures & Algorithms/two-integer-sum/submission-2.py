class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        for i in range(len(nums)):
            diff = target - n[i]
            if need[diff] != None:
                return [need[diff], i]

            need[n[i]] = i
        