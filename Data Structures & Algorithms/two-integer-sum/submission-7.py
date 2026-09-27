class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        need = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in need:
                return [need[diff], i]

            need[nums[i]] = i
        