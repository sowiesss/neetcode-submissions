class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        offset = defaultdict(int)
        for i, n in enumerate(numbers):
            off = target - n
            if off in offset:
                return [offset[off], i + 1]
            offset[n] = i + 1
        return []