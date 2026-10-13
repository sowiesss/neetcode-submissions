class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] >= target:
                r = mid - 1
            if nums[mid] < target:
                l = mid
        
        return r + 1 if r < len(nums) - 1 and nums[r + 1] == target else -1