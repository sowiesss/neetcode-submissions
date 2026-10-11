class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, n= 0, len(numbers)
        r = n - 1
        while l < r:
            s = numbers[l] + numbers[r]
            mid = (l + r) // 2
            if s < target:
                l = mid
            elif s > target:
                r = mid
            else:
                return [l + 1, r + 1]
        return []
