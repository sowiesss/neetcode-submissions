class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r

            mid = (l + r) // 2
            if mid == l:
                break
            if nums[mid] == target:
                return mid

            if nums[mid] > nums[r]:
                if nums[mid] < target:
                    r = mid + 1
                if nums[mid] > target:
                    if nums[r] > target:
                        l = mid + 1
                    if nums[r] < target:
                        r = mid - 1
            if nums[mid] < nums[r]:
                if nums[mid] < target:
                    if nums[r] > target:
                        l = mid + 1
                    if nums[r] < target:
                        r = mid - 1
                if nums[mid] > target:
                    r = mid - 1

        return l if nums[l] == target else -1