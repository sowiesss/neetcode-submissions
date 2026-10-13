class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l)//2
            if nums[mid] > target:
                r = mid
            if nums[mid] <= target:
                l = mid + 1
        
        return l - 1 if l and nums[l - 1] == target else -1