class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while 0 <= l < r < len(numbers):
            # print(l, r)
            while l < r and numbers[l] + numbers[r] > target:
                r -= 1
            # print(r)
            while l < r and numbers[l] + numbers[r] < target:
                l += 1
            # print(l)            
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
        
        return []