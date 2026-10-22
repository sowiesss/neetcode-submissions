class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
           
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[r]:
                if nums[mid] < target or nums[r] >= target:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] > target or nums[r] < target:
                    r = mid - 1
                else: # mid < target and r >= target
                    l = mid + 1

        return l if nums[l] == target else -1