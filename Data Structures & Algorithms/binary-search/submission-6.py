import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect.bisect(nums, target)
        return i - 1 if i and nums[i - 1] == target else -1